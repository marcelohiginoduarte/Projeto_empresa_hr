from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from Fotoscampo.models import FotosCampo, arquivos_foto
from Fotoscampo.forms import FotosCampoform, Projeto_fotoforms, arquivos_fotos_projetoform
from Fotoscampo.Filters import FotoFilter
from django.forms import modelformset_factory
from .serializer import FotoSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from reportlab.pdfgen import canvas
from django.http import Http404
from reportlab.lib.pagesizes import A4
from rest_framework.response import Response
from io import BytesIO
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from Fotoscampo.serializer import FotoSerializer
from django.urls import reverse_lazy


FotocampoFormSet = modelformset_factory(FotosCampo, form=FotosCampoform, extra=1)


def upload_fotos(request):
    if request.method == "POST":
        formset = FotocampoFormSet(
            request.POST, request.FILES, queryset=FotosCampo.objects.none()
        )

        if formset.is_valid():
            formset.save()
            return redirect("vertodasasfotos")
    else:
        formset = FotocampoFormSet(queryset=FotosCampo.objects.none())

    return render(request, "upload_fotos_campo.html", {"formset": formset})



def gerar_pdf_fotos_grupadas(request, projeto_nome):
    arquivos = FotosCampo.objects.filter(projeto=projeto_nome)

    if not arquivos.exists():
        raise Http404("Nenhuma foto encontrada para o projeto.")

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4

    nome_empresa = "JJ Serviços Eletricos"
    titulo_projeto = f"Relatório de Fotos do Projeto: {projeto_nome}"
    numero_pagina = 1
    imagens_por_pagina = 5
    imagens_na_pagina = 0

    def desenhar_legenda(
        canvas_obj, empresa, projeto, altura_atual, pagina_atual, foto
    ):
        canvas_obj.setFont("Helvetica-Bold", 14)
        canvas_obj.drawString(120, altura_atual, f"Empresa: {empresa}")
        canvas_obj.setFont("Helvetica", 12)
        canvas_obj.drawString(50, altura_atual - 20, f"Projeto: {projeto}")
        canvas_obj.drawString(50, altura_atual - 40, "Relatório de Fotos")
        canvas_obj.drawString(50, altura_atual - 60, f"Página: {pagina_atual}")

        if foto:
            x_offset = largura - 250
            canvas_obj.setFont("Helvetica", 10)
            canvas_obj.drawString(
                x_offset, altura_atual - 20, f"Supervisor: {foto.Supervisor}"
            )
            equipe_nome = (
                foto.Equipe.Nome_encarregado if foto.Equipe else "Não atribuída"
            )
            canvas_obj.drawString(x_offset, altura_atual - 40, f"Equipe: {equipe_nome}")
            canvas_obj.drawString(x_offset, altura_atual - 60, f"Cidade: {foto.Cidade}")
            canvas_obj.drawString(
                x_offset, altura_atual - 80, f"Endereço: {foto.Endereco}"
            )
            canvas_obj.drawString(
                x_offset, altura_atual - 100, f"Ocorrência: {foto.ocorrencia}"
            )
            canvas_obj.drawString(x_offset, altura_atual - 120, f"GPS: {foto.GPS}")

        return altura_atual - 140

    y_position = altura - 50

    def draw_images_side_by_side(image_fields, labels, y_pos):
        nonlocal numero_pagina, y_position, imagens_na_pagina

        x_offset = 50
        max_width = 200  #
        gap = 20
        max_images_per_row = 2

        for image_field, label in zip(image_fields, labels):
            if image_field and hasattr(image_field, "path") and image_field.path:
                image_path = image_field.path

                if y_pos - 180 < 50 or imagens_na_pagina >= imagens_por_pagina:
                    p.showPage()
                    numero_pagina += 1
                    y_pos = altura - 50
                    y_pos = desenhar_legenda(
                        p, nome_empresa, titulo_projeto, y_pos, numero_pagina, None
                    )
                    imagens_na_pagina = 0

                p.drawImage(
                    image_path, x_offset, y_pos - 150, width=max_width, height=150
                )
                p.setFont("Helvetica-Bold", 12)
                p.drawString(x_offset, y_pos - 170, label)

                x_offset += max_width + gap

                if x_offset + max_width + gap > largura - 50:
                    x_offset = 50
                    y_pos -= 180
                    imagens_na_pagina += max_images_per_row

                imagens_na_pagina += 1

                if y_pos - 180 < 50:
                    p.showPage()
                    numero_pagina += 1
                    y_pos = altura - 50
                    y_pos = desenhar_legenda(
                        p, nome_empresa, titulo_projeto, y_pos, numero_pagina, None
                    )
                    imagens_na_pagina = 0

        return y_pos

    try:
        for foto in arquivos:
            y_position = desenhar_legenda(
                p, nome_empresa, titulo_projeto, y_position, numero_pagina, foto
            )

            y_position = draw_images_side_by_side(
                [foto.Poste_antes, foto.Poste_depois],
                ["Poste Antes", "Poste Depois"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.cava_antes, foto.cava_depois],
                ["Cava Antes", "Cava Depois"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.GPS_antes, foto.GPS_depois],
                ["GPS Antes", "GPS Depois"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.Estrutura_antes, foto.Estrutura_depois],
                ["Estrutura Antes", "Estrutura Depois"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.panoramica, foto.Equipamento_antes],
                ["Panorâmica", "Equipamento Antes"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.Equipamento_depois, foto.Numero_serie_antes],
                ["Equipamento Depois", "Número Série Antes"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.Numero_serie_depois, foto.Numero_sap_antes],
                ["Número Série Depois", "Número SAP Antes"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.Numero_sap_depois, foto.Numero_placa_antes],
                ["Número SAP Depois", "Número Placa Antes"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.Numero_placa_depois, foto.Poda_antes],
                ["Número Placa Depois", "Poda Antes"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.Poda_depois, foto.concreto_calcada_antes],
                ["Poda Depois", "Concreto Calçada Antes"],
                y_position,
            )
            y_position = draw_images_side_by_side(
                [foto.concreto_calcada_depois], ["Concreto Calçada Depois"], y_position
            )

    except Exception as e:
        raise Http404(f"Erro ao gerar o PDF: {str(e)}")

    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type="application/pdf")


def permission_denied_view(request, exception):
    return render(request, "403.html", status=403)




@login_required
@permission_required("GestaoHR.acesso_fotoscampo", raise_exception=True)
def verfotos(request):
    fotos = FotosCampo.objects.all()
    filterset = FotoFilter(request.GET, queryset=fotos)
    projetos_exibidos = set()
    fotos_unicas = []

    for foto in filterset.qs:
        if foto.projeto not in projetos_exibidos:
            fotos_unicas.append(foto)
            projetos_exibidos.add(foto.projeto)

    context = {
        "fotos": fotos_unicas,
        "filterset": filterset,
    }
    return render(request, "vertodasfotos.html", context)


def verfotos_grupadas(request, projeto_nome):
    arquivos = FotosCampo.objects.filter(projeto=projeto_nome)
    print(f"Arquivos encontrados: {arquivos.count()} para o projeto {projeto_nome}")

    return render(
        request,
        "fotos_campo.html",
        {
            "projeto_nome": projeto_nome,
            "arquivos": arquivos,
        },
    )


# Fotos pequenas


@login_required
@permission_required("GestaoHR.acesso_fotoscampo", raise_exception=True)
def fotos_campo_view(request, pk):
    arquivos = get_object_or_404(FotosCampo, pk=pk)
    contexto = {"arquivos": arquivos}
    return render(request, "fotos_campo.html", contexto)


@login_required
@permission_required("GestaoHR.acesso_fotoscampo", raise_exception=True)
def Salvar_projeto_foto(request):
    erro = None
    texto = None

    if request.method == "POST":
        form = Projeto_fotoforms(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("salvarprojetofoto")
    else:
        form = Projeto_fotoforms()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    return render(
        request, "salvarprojetofoto.html", {"form": form, "erro": erro, "texto": texto}
    )



