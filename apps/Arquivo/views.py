from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from Arquivo.models import Aquivo
from Arquivo.forms import testform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from Arquivo.filters import AquivoFilter
from django_filters.views import FilterView



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
