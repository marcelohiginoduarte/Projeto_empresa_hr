from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from GestaoHR.models import (
    collaborator,
    Aquivo,
    Servico,
    DemandaInterna,
    BancoArquivos,
    FotosCampo,
    arquivos_foto,
    SESMT,
    ArquivoSesmt,
    Document,
    Produto,
    MovimentacaoEstoque,
    Caderno_servico,
    Equipe,
    ProgramacaoEquipes,
    ItemServico,
)
from django.urls import reverse_lazy
from .forms import (
    CollaboratorForm,
    testform,
    Servicoform,
    DemandaInternaform,
    BancoArquivoform,
    FotosCampoform,
    FotocampoFormSet,
    SESMTFORM,
    ArquivoSesmtForm,
    Projeto_fotoforms,
    arquivos_fotos_projetoform,
    DocumentForm,
    MovimentacaoForm,
    CadastrarProduto,
    CadastraEquipeform,
    ProgramacaoEquipeForm,
)
from datetime import datetime
from .filters import (
    collaboratorFilter,
    AquivoFilter,
    ArquivoFilter,
    ServicoFilter,
    DemandaFilter,
    FotoFilter,
)
from django_filters.views import FilterView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
import pandas as pd
from django.http import FileResponse, Http404
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import modelformset_factory
from django.contrib import messages
from .serializer import FotoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.views.decorators.debug import sensitive_variables
import io
from .utils import carregar_planilha_caderno_servico, buscar_informacoes
from docx import Document
import pypandoc
from io import BytesIO


@login_required
def home(request):
    return render(
        request,
        "home.html",
    )


@login_required
@permission_required("GestaoHR.acesso_rh", raise_exception=True)
def create_Collaborator(request):

    erro = None
    texto = None

    if request.method == "POST":
        form = CollaboratorForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("viewcollaborator")
    else:
        form = CollaboratorForm()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    def clean(self):
        self.validate_CPF()

    # validar o CPF.
    def validate_CPF(self):
        CPF = self.CPF
        if not CPF.isdigit() or len(CPF) != 11:
            raise ValidationError("O CPF deve conter 11 dígitos.")

    return render(
        request, "register.html", {"form": form, "erro": erro, "texto": texto}
    )


@login_required
@permission_required("GestaoHR.acesso_rh", raise_exception=True)
def to_view_collaborator(request):
    if not request.user.has_perm("app_name.pode_ver_pagina"):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect("homapage")  
    view_collaborator = collaboratorFilter(
        request.GET, queryset=collaborator.objects.all()
    )
    return render(
        request, "view_collaborator.html", {"collaboratorfilter": view_collaborator}
    )


# Deletar colaborador


class DeletarColaborador(DeleteView):
    model = collaborator
    template_name = "colaborador__confirm_delete.html"
    success_url = reverse_lazy("viewcollaborator")


@login_required
@permission_required("GestaoHR.acesso_rh", raise_exception=True)
def detalhe_fucionario(request, pk):
    colaboradores = get_object_or_404(collaborator, pk=pk)
    data_ferias = colaboradores.calcular_data_ferias()
    return render(
        request,
        "view_collaborator.html",
        {"colaboradores": colaboradores, "data_ferias": data_ferias},
    )


class FazerUpdate(UpdateView):
    model = collaborator
    template_name = "update_collaborator.html"
    fields = [
        "Nome",
        "CPF",
        "RG",
        "Data_contratacao",
        "Servico",
        "CNH",
        "Vencimento_CNH",
        "Data_contratacao",
        "Data_ferias",
        "matricula",
        "ASO",
        "validade_aso",
        "PIS",
        "Salario",
        "Controle_folha_ponto",
        "Seguro_de_vida",
    ]
    success_url = reverse_lazy("viewcollaborator")


class VisualizarCollaborator(ListView):
    model = collaborator
    template_name = "visuzalizar.html"
    fields = [
        "Nome",
        "CPF",
        "RG",
        "Data_contratacao",
        "Servico",
        "CNH",
        "Vencimento_CNH",
        "Data_contratacao",
        "Data_ferias",
        "matricula",
        "ASO",
        "validade_aso",
        "PIS",
        "Salario",
        "Controle_folha_ponto",
        "Seguro_de_vida",
    ]
    paginate_by = 10
    success_url = reverse_lazy("viewcollaborator")


@login_required
@permission_required("GestaoHR.acesso_rh", raise_exception=True)
def to_view_collaborator1(request):
    view_collaborator = collaboratorFilter(
        request.GET, queryset=collaborator.objects.all()
    )
    return render(
        request, "visuzalizar.html", {"collaboratorFilter": view_collaborator}
    )


@login_required
@permission_required("GestaoHR.acesso_rh", raise_exception=True)
def listar_nomes(FilterView):
    model = collaborator
    context_object_name = "Nome"
    filterset_class = collaboratorFilter
    template_name = "vizualizar.html"


@login_required
@permission_required("GestaoHR.acesso_rh", raise_exception=True)
def uploadfotos(request):
    if request.method == "POST":
        form = testform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("folhadeponto")
    else:
        form = testform()
        return render(request, "folhadeponto.html", {"form": form})


@login_required
@permission_required("GestaoHR.acesso_rh", raise_exception=True)
def visualizar_folhas_ponto(request):
    visualizar_folhas = AquivoFilter(request.GET, queryset=Aquivo.objects.all())
    return render(
        request, "visualizar_folhas.html", {"AquivoFilter": visualizar_folhas}
    )


class listar_nomestc(FilterView):
    model = Aquivo
    filterset_class = AquivoFilter
    template_name = "visualizar_folhas.html"
    context_object_name = "aquivo"


@login_required
@permission_required("GestaoHR.acesso_rh", raise_exception=True)
def visualizar_com_id(request, pk):
    objeto = get_object_or_404(collaborator, pk=pk)
    contexto = {"objeto": objeto}
    return render(request, "visuzalizar.html", contexto)


class DetalheView(DetailView):
    model = collaborator
    template_name = "visualizar_colaborador_unitario.html"
    context_object_name = "objeto"


# Inicio dos Serviços


# cadastrar novos serviços
@login_required
@permission_required("GestaoHR.acesso_servicos", raise_exception=True)
def create_servico(request):
    erro = None
    texto = None

    if request.method == "POST":
        form = Servicoform(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("visualizartodosservios")
    else:
        form = Servicoform()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    return render(
        request, "servico_register.html", {"form": form, "erro": erro, "texto": texto}
    )


# Remover Serviço


class ServicoDelete(DeleteView):
    model = Servico
    template_name = "servico__confirm_delete.html"
    success_url = reverse_lazy("visualizartodosservios")


# visualizar serviços


@login_required
@permission_required("GestaoHR.acesso_servicos", raise_exception=True)
def visualiazer_servicos(request):
    visualizar_sd = ServicoFilter(request.GET, queryset=Servico.objects.all())
    paginator = Paginator(visualizar_sd.qs, 20)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "servico_view.html",
        {"ServicoFilter": visualizar_sd, "page_obj": page_obj},
    )


# preencher status automatico


@receiver(post_save, sender=Servico)
def preencher_formulario(sender, instance, **kwargs):
    if instance.Status == "Fechamento":
        DemandaInterna.objects.create(
            Atividade=instance.Numero_Servico,  # Acessa o campo da instância atual
            tipo="Aguardando",
            responsavel="",
            status="Aguardando",
            Observacao="Obra executada, Atenção incluir as informações para fechamento.",
            data_solicitacao=datetime.now().date(),  # Passa a data diretamente
        )


# pagina de serviços


@login_required
@permission_required("GestaoHR.acesso_servicos", raise_exception=True)
def listar_servico_paginas(request):
    todos = Servico.objects.all()
    paginator = Paginator(todos, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "servico_view.html", {"page_obj": page_obj})


# Update em Serviços


class ServicoUpdate(UpdateView):
    model = Servico
    template_name = "servico_update.html"
    fields = [
        "Numero_Servico",
        "Valor_pago",
        "Requisicao_ODD",
        "Requisicao_ODI",
        "Medicao",
        "As_built",
        "AES_ACOS",
        "evidencias",
        "tecnico",
        "Status",
        "tipo_servico",
        "Equipe",
        "Status_SAP",
        "Tipo_investimento",
        "PEP",
        "Servico",
        "Mês_servico",
        "Ano_servico",
        "data_da_solicitacao",
        "Municipio",
        "Endereco",
        "Status",
        "data_programacao",
        "Valor_parcial",
        "Valor_final",
        "desenho_servico",
        "foto_antes",
        "foto_depois",
        "Observacao",
    ]
    success_url = reverse_lazy("visualizartodosservios")


class ServicoUpdateStatus(UpdateView):
    model = Servico
    template_name = "servico_update.html"
    fields = ["Status"]
    success_url = reverse_lazy("visualizartodosservios")


@login_required
@permission_required("GestaoHR.acesso_servicos", raise_exception=True)
def servico_update_servico(request, pk):
    servicos = get_object_or_404(Servico, pk=pk)
    contexto = {"servicos": servicos}
    return render(request, "servico_update.html", contexto)


# visualiazar serviço unitario
@login_required
@permission_required("GestaoHR.acesso_servicos", raise_exception=True)
def servico_visualizar_com_id(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    contexto = {"servico": servico}
    return render(request, "servico_unitario.html", contexto)


class ServicoView(DetailView):
    model = Servico
    template_name = "servico_unitario.html"
    context_object_name = "servico"


# contar serviço


@login_required
@permission_required("GestaoHR.acesso_servicos", raise_exception=True)
def intem_lista(request):
    contar_andamento = Servico.objects.filter(Status="Andamento").count()
    contar_programacao = Servico.objects.filter(Status="Programação").count()
    contar_espera = Servico.objects.filter(Status="Espera").count()
    Concluido = Servico.objects.filter(Status="Concluido").count()
    Fechamento = Servico.objects.filter(Status="Fechamento").count()
    Pagamento = Servico.objects.filter(Status="Pagamento").count()
    Recebido = Servico.objects.filter(Status="Recebido").count()

    context = {
        "contar_andamento": contar_andamento,
        "somar_andamento": Servico.somar_valor_status("Andamento"),
        "somar_programacao": Servico.somar_valor_status("Programação"),
        "somar_concluido": Servico.somar_valor_status("Concluido"),
        "somar_Fechamento": Servico.somar_valor_status("Fechamento"),
        "somar_Pagamento": Servico.somar_valor_status("Pagamento"),
        "somar_Espera": Servico.somar_valor_status_parcial("Espera"),
        "somar_Recebido": Servico.somar_valor_status("Recebido"),
        "contar_programacao": contar_programacao,
        "contar_espera": contar_espera,
        "Pagamento": Pagamento,
        "Concluido": Concluido,
        "Fechamento": Fechamento,
        "Recebido": Recebido,
    }
    return render(request, "servico_dashboard.html", context)


# SOmar valores


def somar_valor_status(request):
    somar_andamento = Servico.objects.filter(Status="Andamento").aggregate(
        valor_andamento=Sum("Valor_final")
    )

    context = {"valor_andamento": somar_andamento["valor_andamento"] or 0}

    return render(request, "servico_dashboard.html", context)


# Demanda Internas


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


# Banco de arquivos


@login_required
def CreateArquivos(request):
    erro = None
    texto = None

    if request.method == "POST":
        form = BancoArquivoform(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("visualizararquivos")
    else:
        form = BancoArquivoform()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    return render(
        request, "arquivos_criar.html", {"form": form, "erro": erro, "texto": texto}
    )


@login_required
def visualizar_arquivos(request):
    arquivos = ArquivoFilter(request.GET, queryset=BancoArquivos.objects.all())
    return render(request, "arquivos_visualizartd.html", {"ArquivoFilter": arquivos})


class ArquivoUodate(UpdateView):
    model = BancoArquivos
    template_name = "arquivo_update.html"
    fields = [
        "EI_OC",
        "tipo",
        "municipio",
        "AS_Biult",
        "Responsavel",
        "Medicao",
        "DWG",
        "AES",
        "ACOS",
    ]
    success_url = "visualizararquivos"


@login_required
def atualizar_arquivos(request, pk):
    arquivos = get_object_or_404(BancoArquivos, pk=pk)
    contexto = {"arquivos": arquivos}
    return render(request, "arquivo_update.html", contexto)


# Arquivoviews


class ArquivoViews(DetailView):
    model = BancoArquivos
    template_name = "arqvuivo_unitario.html"
    context_object_name = "detalhe"

    def get_success_url(self):
        return reverse_lazy("#", kwargs={"pk": self.object.pk})


# filtro


@login_required
def arquivo_filtro(request):
    filtro = BancoArquivos.objects.all()
    return render(request, "arquivos_visualizartd.html", {"filtro": filtro})


# login


@sensitive_variables("password")
def logar(request):
    if request.user.is_authenticated:
        return redirect("homapage")
    if request.method != "POST":
        return render(request, "login_teste.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("homapage")
    else:
        return render(
            request, "login_teste.html", {"error_message": "Login ou senha inválidos"}
        )
    return render(request, "base.html")


# exportar execel colaborador


def exportar_para_execel_colaboradores(request):
    colaboradores_excel = collaborator.objects.all().values()
    df = pd.DataFrame(colaboradores_excel)
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="colaboradores_excel.xlsx"'
    df.to_excel(response, index=False)
    return response


# exportar execel serviços


def servico_exportar_execel(request):
    servico_execel = Servico.objects.all().values()
    df = pd.DataFrame(servico_execel)
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="servico_excel.xlsx"'
    df.to_excel(response, index=False)
    return response


# exportar execel Demandas internas


def demandainterna_exportar_execel(request):
    demandainterna_execel = DemandaInterna.objects.all().values()
    df = pd.DataFrame(demandainterna_execel)
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="demandainterna_excel.xlsx"'
    df.to_excel(response, index=False)
    return response


def logout_view(request):
    logout(request)
    return redirect("homapage")


# FOTOS DE CAMPO
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


# SESMT
# criar arquivos
@login_required
def crearsesmt(request):
    erro = None
    texto = None

    if request.method == "POST":
        form = SESMTFORM(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("mostrararquivossesmt")
    else:
        form = SESMTFORM()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    return render(request, "SESMT.html", {"form": form, "erro": erro, "texto": texto})


# Ver os arquivos


@login_required
def versesmt(request):
    arquivos = SESMT.objects.all()
    return render(request, "sesmt_ver.html", {"arquivos": arquivos})


# novos arquivos sesmt


@login_required
def atualizararquivo(request, arquivo_id):
    arquivo_antigo = get_object_or_404(ArquivoSesmt, id=arquivo_id)

    if request.method == "POST":
        form = ArquivoSesmtForm(request.POST, request.FILE)
        if form.is_valid():
            novo_arquivo = form.save(commit=False)
            novo_arquivo.versao_anterior = arquivo_antigo
            novo_arquivo.save()
            return redirect("listadearquivos")
    else:
        form = ArquivoSesmtForm()

    return render(
        request, "arquivossesmt.html", {"form": form, "arquivo_antigo": arquivo_antigo}
    )


# Update SESMT


class SesmtUpdate(UpdateView):
    model = SESMT
    template_name = "sesmt_update.html"
    fields = [
        "Brigada_emergerncia",
        "CIPA",
        "CNPJ_CRB",
        "CRB",
        "Documentacao_veiculo",
        "manual_veiculo",
        "orcamentos",
        "PCSMO",
        "prg",
        "plano_de_atendimento_emergencia",
        "plano_de_manutencao_frota",
        "POP_lM_construcao",
        "POP_LV_contrucao",
        "POP_sesmt",
        "PPCI",
        "SESMT_t",
        "Ultima_atualização",
    ]
    success_url = reverse_lazy("mostrararquivossesmt")


# salvar projeto para foto


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


# verfotos


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


# verprojetoativo


@login_required
@permission_required("GestaoHR.acesso_fotoscampo", raise_exception=True)
def verprojetoativo(request):
    projetos_ativos = FotoFilter(request.GET, queryset=FotosCampo.objects.all())
    filtro = projetos_ativos.qs
    return render(
        request,
        "verprojetosativos.html",
        {"FotoFilter": projetos_ativos, "filtro": filtro},
    )


# update ativos


class atualizativo(UpdateView):
    model = arquivos_foto
    template_name = "arquivofotoprojetoutdate.html"
    form_class = arquivos_fotos_projetoform
    success_url = reverse_lazy("projetoativo")


# deletar Projeto


class Deletarprojeto(DeleteView):
    model = arquivos_foto
    template_name = "arquivofotodemanda__confirm_delete.html"
    success_url = reverse_lazy("projetoativo")


# teste


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = "document_form.html"
    success_url = "/success/"


class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = "document_form.html"
    success_url = "/success/"


class DocumentListView(ListView):
    model = Document
    template_name = "document_list.html"
    context_object_name = "documents"


@login_required
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "estoque_listarprodutos.html", {"produtos": produtos})


@login_required
@permission_required("GestaoHR.acesso_gestaoestoque", raise_exception=True)
def movimentacao_estoque(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == "POST":
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.produto = produto
            if movimentacao.tipo == "ENTRADA":
                produto.quantidade += movimentacao.quantidade
            elif (
                movimentacao.tipo == "SAIDA"
                and produto.quantidade >= movimentacao.quantidade
            ):
                produto.quantidade -= movimentacao.quantidade
            produto.save()
            movimentacao.save()
            return redirect("listarestoque")
    else:
        form = MovimentacaoForm()
    return render(
        request, "estoque_movimentacao_estoque.html", {"produto": produto, "form": form}
    )


@login_required
@permission_required("GestaoHR.acesso_gestaoestoque", raise_exception=True)
def cadastra_produto(request):
    erro = None
    texto = None

    if request.method == "POST":
        form = CadastrarProduto(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("listarestoque")
    else:
        form = CadastrarProduto()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    return render(
        request,
        "estoque_cadastrar_produto.html",
        {"form": form, "erro": erro, "texto": texto},
    )


@login_required
@permission_required("GestaoHR.acesso_gestaoestoque", raise_exception=True)
def registro_movimentacao(request):
    movimentacao = MovimentacaoEstoque.objects.all()
    return render(
        request, "estoque_registromovimentacao.html", {"movimentacao": movimentacao}
    )


# receberfotodopost


class FotoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        fotos = FotosCampo.objects.all()
        serializer = FotoSerializer(fotos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("Dados recebidos:", request.data)
        print("Arquivos recebidos:", request.FILES)

        # Verifica se o campo 'Poste_antes' está presente
        if "Poste_antes" not in request.FILES:
            return Response(
                {"error": "Campo 'Poste_antes' não encontrado na requisição."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = FotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Erros de validação:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


def cadastrar_equipe(request):

    erro = None
    texto = None

    if request.method == "POST":
        form = CadastraEquipeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("vertodasequipes")
    else:
        form = CadastraEquipeform()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    return render(
        request, "equipe_cadastrar.html", {"form": form, "erro": erro, "texto": texto}
    )


def ver_equipes(request):
    equipes = Equipe.objects.all()
    return render(request, "equipes_vertodas.html", {"equipes": equipes})


class AtualizarEquipe(UpdateView):
    model = Equipe
    template_name = "equipe_atualizar.html"
    form_class = CadastraEquipeform
    success_url = reverse_lazy("vertodasequipes")


class DeletarEquipe(DeleteView):
    model = Equipe
    template_name = "equipe__confirm_delete.html"
    success_url = reverse_lazy("vertodasequipes")


@login_required
def cadastrar_programacaoequipe(request):

    erro = None
    texto = None

    if request.method == "POST":
        form = ProgramacaoEquipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("vertodaprogramacao")
    else:
        form = ProgramacaoEquipeForm()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    return render(
        request,
        "programacao_cadastrar.html",
        {"form": form, "erro": erro, "texto": texto},
    )


def ver_programacao(request):
    programacoes = ProgramacaoEquipes.objects.all()
    return render(request, "programacao_vertodas.html", {"programacoes": programacoes})


class AtualizarProgramacaoEquipes(UpdateView):
    model = ProgramacaoEquipes
    template_name = "programacao_equipe_atualizar.html"
    form_class = ProgramacaoEquipeForm
    success_url = reverse_lazy("vertodaprogramacao")


class DeletarProgramacaoEquipes(DeleteView):
    model = ProgramacaoEquipes
    template_name = "equipe__confirm_delete.html"
    success_url = reverse_lazy("vertodaprogramacao")


def calendario_view(request):
    tarefas = ProgramacaoEquipes.objects.all()

    calendario = {}
    for tarefa in tarefas:
        dia = tarefa.dia
        mes = tarefa.Mes
        if mes not in calendario:
            calendario[mes] = {}
        if dia not in calendario[mes]:
            calendario[mes][dia] = []
        calendario[mes][dia].append(
            {"SI_OC": tarefa.SI_OC, "Encarregado": tarefa.Encarregado}
        )

    return render(request, "programacao_calendario.html", {"calendario": calendario})


def calendario_dados(request):
    tarefas = ProgramacaoEquipes.objects.all()

    eventos = []
    for tarefa in tarefas:
        eventos.append(
            {
                "title": f"{tarefa.SI_OC} - {tarefa.Encarregado}",
                "start": f"{tarefa.ANO}-{tarefa.Mes.zfill(2)}-{tarefa.dia.zfill(2)}",
                "allDay": True,
            }
        )

    return JsonResponse(eventos, safe=False)


def importar_planilha(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    for _, row in df.iterrows():
        item = ItemServico(
            codigo=row["Codigo"],
            descricao=row["Descricao"],
            valor_unitario=row["Valor Unitario"],
        )
        item.save()


def adicionar_medicao(request):
    valor_acumulado = 0
    if request.method == "POST":
        form = ItemServico(request.POST)
        if form.is_valid():
            form.save()

            valor_acumulado += form.instance.valor_total
            return redirect("lista_medicoes")

    form = MedicaoForm()
    return render(
        request,
        "adicionar_medicao.html",
        {"form": form, "valor_acumulado": valor_acumulado},
    )
