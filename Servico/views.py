from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Servico
from Servico.filters import ServicoFilter
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from Servico.models import Servico
from Equipe.models import Equipe 
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import Servicoform
import pandas as pd



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


def servico_exportar_execel(request):
    servico_execel = Servico.objects.all().values()
    df = pd.DataFrame(servico_execel)
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="servico_excel.xlsx"'
    df.to_excel(response, index=False)
    return response