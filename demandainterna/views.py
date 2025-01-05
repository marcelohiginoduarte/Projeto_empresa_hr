from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from demandainterna.models import DemandaInterna
from demandainterna.forms import DemandaInternaform
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
import pandas as pd
from demandainterna.filters import DemandaFilter


@login_required
@permission_required("GestaoHR.acesso_demandaInterna2", raise_exception=True)
def createdemanda(request):
    erro = None
    texto = None

    if request.method == "POST":
        form = DemandaInternaform(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("Demandainternaviews")
    else:
        form = DemandaInternaform()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    return render(
        request,
        "demanadainterna_criar.html",
        {"form": form, "erro": erro, "texto": texto},
    )


# Update em demandas internas


class DemandaUpdate(UpdateView):
    model = DemandaInterna
    template_name = "demandainterna_update.html"
    form_class = DemandaInternaform
    success_url = reverse_lazy("Demandainternaviews")


@login_required
@permission_required("GestaoHR.acesso_demandaInterna2", raise_exception=True)
def demanda_interna_update(request, pk):
    demandas = get_object_or_404(DemandaInterna, pk=pk)
    contexto = {"demandas": demandas}
    return render(request, "demandainterna_update.html", contexto)


# visualaizar todas


@login_required
@permission_required("GestaoHR.acesso_demandaInterna2", raise_exception=True)
def demandainternavisualizartd(request):
    demanda = DemandaFilter(
        request.GET, queryset=DemandaInterna.objects.all().order_by("status")
    )
    paginator = Paginator(demanda.qs, 20)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "demandainterna_views.html",
        {"DemandaFilter": demanda, "page_obj": page_obj},
    )


# auterar status demanda interna


class DemandainternaStatus(UpdateView):
    model = DemandaInterna
    template_name = "demandainterna_update.html"
    fields = ["status"]
    success_url = reverse_lazy("Demandainternaviews")


# Remover Demanada Interna


class RemoverDemanda(DeleteView):
    model = DemandaInterna
    template_name = "demanda__confirm_delete.html"
    success_url = reverse_lazy("Demandainternaviews")


# Dash demanda interna


def dashdemandainterna(request):
    contaraguardando = DemandaInterna.objects.filter(status="Aguardando").count()
    contarAndamento = DemandaInterna.objects.filter(status="Andamento").count()
    contarRealizado = DemandaInterna.objects.filter(status="Realizado").count()
    contarCorreção = DemandaInterna.objects.filter(status="Correção").count()
    contarEnviadoEquatorial = DemandaInterna.objects.filter(
        status="Enviado Equatorial"
    ).count()
    contarAprovadoEquatorial = DemandaInterna.objects.filter(
        status="Aprovado Equatorial"
    ).count()
    contarCorreçãoEquatorial = DemandaInterna.objects.filter(
        status="Correção Equatorial"
    ).count()
    contarAguardandoEquatorial = DemandaInterna.objects.filter(
        status="Aguardando Equatorial"
    ).count()

    context = {
        "contaraguardando": contaraguardando,
        "contarAndamento": contarAndamento,
        "contarRealizado": contarRealizado,
        "contarCorreção": contarCorreção,
        "contarEnviadoEquatorial": contarEnviadoEquatorial,
        "contarAprovadoEquatorial": contarAprovadoEquatorial,
        "contarCorreçãoEquatorial": contarCorreçãoEquatorial,
        "contarAguardandoEquatorial": contarAguardandoEquatorial,
    }

    return render(request, "demanda_dashboard.html", context)



def demandainterna_exportar_execel(request):
    demandainterna_execel = DemandaInterna.objects.all().values()
    df = pd.DataFrame(demandainterna_execel)
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="demandainterna_excel.xlsx"'
    df.to_excel(response, index=False)
    return response


@login_required
@permission_required("GestaoHR.acesso_demandaInterna2", raise_exception=True)
def consultar_servico(request):
    if request.method == "POST":
        nome_servico = request.POST.get("nome_servico")

        planilha = Caderno_servico.objects.first()
        if planilha:
            df = carregar_planilha_caderno_servico(planilha.arquivo.path)
            informacoes = buscar_informacoes(df, nome_servico)

            if informacoes.empty:
                return render(
                    request,
                    "medicao_resultado.html",
                    {"error": "Serviço não encontrado"},
                )
            else:
                return render(
                    request,
                    "medicao_resultado.html",
                    {"informacoes": informacoes.to_dict(orient="records")},
                )

    return render(request, "medicao_consulta.html")

def preencher_acos(request):
    if request.method == "POST":
        numero_projeto = request.POST.get("numero_projeto")
        data_conclusao = request.POST.get("data_conclusao")
        endereco = request.POST.get("endereco")
        data_assinatura = request.POST.get("data_assinatura")

        doc = Document("media/media/acos/ACOS.docx")

        for paragraph in doc.paragraphs:
            if "[NUMERO_PROJETO]" in paragraph.text:
                paragraph.text = paragraph.text.replace(
                    "[NUMERO_PROJETO]", numero_projeto
                )
            if "[DATA_CONCLUSAO]" in paragraph.text:
                paragraph.text = paragraph.text.replace(
                    "[DATA_CONCLUSAO]", data_conclusao
                )
            if "[ENDERECO]" in paragraph.text:
                paragraph.text = paragraph.text.replace("[ENDERECO]", endereco)
            if "[DATA_ASSINATURA]" in paragraph.text:
                paragraph.text = paragraph.text.replace(
                    "[DATA_ASSINATURA]", data_assinatura
                )

        doc_path = "media/media/modificado/ACOS.docx"
        doc.save(doc_path)

        pdf_path = "media/media/modificado/ACOS.pdf"
        pypandoc.convert_file(doc_path, "pdf", outputfile=pdf_path)

        pdf_buffer = io.BytesIO()
        with open(pdf_path, "rb") as pdf_file:
            pdf_buffer.write(pdf_file.read())
        pdf_buffer.seek(0)

        return FileResponse(
            pdf_buffer, as_attachment=True, filename="projeto_concluido.pdf"
        )

    return render(request, "acos.html")