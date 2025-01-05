from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from Sesmt.models import SESMT, ArquivoSesmt, Document
from Sesmt.forms import SESMTFORM, ArquivoSesmtForm, DocumentForm


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


@login_required
def versesmt(request):
    arquivos = SESMT.objects.all()
    return render(request, "sesmt_ver.html", {"arquivos": arquivos})


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
