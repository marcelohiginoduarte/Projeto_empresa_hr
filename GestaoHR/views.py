from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from GestaoHR.models import (
    collaborator,
    BancoArquivos,
    arquivos_foto,
    Caderno_servico,
    ItemServico,
)
from django.urls import reverse_lazy
from .forms import (
    CollaboratorForm,
    BancoArquivoform,
)
from datetime import datetime
from .filters import (
    collaboratorFilter,
    ArquivoFilter,
)
from django_filters.views import FilterView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
import pandas as pd
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import modelformset_factory
from django.contrib import messages


from django.views.decorators.debug import sensitive_variables
import io
from .utils import carregar_planilha_caderno_servico, buscar_informacoes
from docx import Document
import pypandoc



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

def permission_denied_view(request, exception):
    return render(request, "403.html", status=403)

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
def visualizar_com_id(request, pk):
    objeto = get_object_or_404(collaborator, pk=pk)
    contexto = {"objeto": objeto}
    return render(request, "visuzalizar.html", contexto)


class DetalheView(DetailView):
    model = collaborator
    template_name = "visualizar_colaborador_unitario.html"
    context_object_name = "objeto"

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


def logout_view(request):
    logout(request)
    return redirect("homapage")


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
