from django.shortcuts import render, redirect, get_object_or_404
from Bancoarquivos.models import BancoArquivos
from Bancoarquivos.forms import BancoArquivoform
from Bancoarquivos.filters import ArquivoFilter
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required


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


class ArquivoViews(DetailView):
    model = BancoArquivos
    template_name = "arqvuivo_unitario.html"
    context_object_name = "detalhe"

    def get_success_url(self):
        return reverse_lazy("#", kwargs={"pk": self.object.pk})


@login_required
def arquivo_filtro(request):
    filtro = BancoArquivos.objects.all()
    return render(request, "arquivos_visualizartd.html", {"filtro": filtro})

