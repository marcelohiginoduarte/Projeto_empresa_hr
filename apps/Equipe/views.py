from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from Equipe.models import Equipe
from Equipe.forms import CadastraEquipeform
from django.views.generic import ListView, UpdateView, CreateView, DeleteView


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


# Create your views here.
