from django.shortcuts import render, redirect
from Programacao.models import ProgramacaoEquipes
from Programacao.forms import ProgramacaoEquipeForm
from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse



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
