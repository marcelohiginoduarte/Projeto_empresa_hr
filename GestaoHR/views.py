from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from GestaoHR.models import collaborator, Aquivo, Servico, DemandaInterna, BancoArquivos
from django.urls import reverse_lazy
from .forms import CollaboratorForm, testform, Servicoform, DemandaInternaform, BancoArquivoform
from datetime import datetime, timedelta
from .filters import collaboratorFilter, AquivoFilter, ArquivoFilter, ServicoFilter,DemandaFilter
from django_filters.views import FilterView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import pandas as pd
from django.http import HttpResponse
from django.db.models import Sum
from asgiref.sync import sync_to_async
from django.db.models.signals import post_save
from django.dispatch import receiver


def home(request):
    return render(request, 'home.html',)

@login_required
def create_Collaborator(request):
    erro = None
    texto = None

    if request.method == "POST":
        form = CollaboratorForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            #form.instance.Data_ferias = form.instance.Data_contratacao + timedelta(days=365)
            form.save()
            return redirect('viewcollaborator')
    else:
        form = CollaboratorForm()
        erro = request.GET.get('erro')
        texto = request.GET.get('texto')

    def clean(self):
        self.validate_CPF()

    #validar o CPF.
    def validate_CPF(self):
        CPF = self.CPF
        if not CPF.isdigit() or len(CPF) != 11:
            raise ValidationError("O CPF deve conter 11 dígitos.")

    return render(request, 'register.html', {'form': form, 'erro': erro, 'texto': texto})

@login_required
def to_view_collaborator(request):
    view_collaborator =collaboratorFilter(request.GET, queryset=collaborator.objects.all())
    return render(request, 'view_collaborator.html', {'collaboratorfilter':view_collaborator })

#Deletar colaborador

class DeletarColaborador(DeleteView):
    model = collaborator
    template_name = 'colaborador__confirm_delete.html'
    success_url = reverse_lazy('viewcollaborator')

@login_required
def detalhe_fucionario(request, pk):
    colaboradores = get_object_or_404(collaborator, pk=pk)
    data_ferias = colaboradores.calcular_data_ferias()
    return render(request, 'view_collaborator.html', {'colaboradores':colaboradores, 'data_ferias':data_ferias})


class FazerUpdate(UpdateView):
    model = collaborator
    template_name = 'update_collaborator.html'
    fields = ['Nome', 'CPF', 'RG', 'Data_contratacao', 'Servico', 'CNH', 'Vencimento_CNH', 'Data_contratacao', 'Data_ferias', 'matricula', 'ASO', 'validade_aso', 'PIS', 'Salario', 'Controle_folha_ponto', 'Seguro_de_vida']
    success_url = reverse_lazy('viewcollaborator')



class VisualizarCollaborator(ListView):
    model = collaborator
    template_name = 'visuzalizar.html'
    fields = ['Nome', 'CPF', 'RG', 'Data_contratacao', 'Servico', 'CNH', 'Vencimento_CNH', 'Data_contratacao', 'Data_ferias', 'matricula', 'ASO', 'validade_aso', 'PIS', 'Salario', 'Controle_folha_ponto', 'Seguro_de_vida']
    paginate_by = 10
    success_url = reverse_lazy('viewcollaborator')

@login_required
def to_view_collaborator1(request):
    view_collaborator = collaboratorFilter(request.GET, queryset= collaborator.objects.all())
    return render(request, 'visuzalizar.html', {'collaboratorFilter':view_collaborator})

@login_required
def listar_nomes(FilterView):
    model=collaborator
    context_object_name = 'Nome'
    filterset_class=collaboratorFilter
    template_name = 'vizualizar.html'

@login_required
def uploadfotos(request):
    if request.method == 'POST':
        form = testform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('folhadeponto')
    else:
        form = testform()
        return render(request, 'folhadeponto.html', {'form': form})
    

@login_required
def visualizar_folhas_ponto(request):
    visualizar_folhas =AquivoFilter(request.GET, queryset= Aquivo.objects.all())
    return render(request, 'visualizar_folhas.html', {'AquivoFilter':visualizar_folhas})


class listar_nomestc(FilterView):
    model=Aquivo
    filterset_class = AquivoFilter
    template_name = 'visualizar_folhas.html'
    context_object_name = 'aquivo'

@login_required
def visualizar_com_id(request, pk):
    objeto = get_object_or_404(collaborator, pk=pk)
    contexto = {'objeto':objeto}
    return render(request, 'visuzalizar.html', contexto)


class DetalheView(DetailView):
    model = collaborator
    template_name = 'visualizar_colaborador_unitario.html'
    context_object_name = 'objeto'


#Inicio dos Serviços

#cadastrar novos serviços
@login_required
def create_servico(request):
    erro = None
    texto = None

    if request.method == 'POST':
        form = Servicoform(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('visualizartodosservios')
    else:
        form = Servicoform()
        erro = request.GET.get('erro')
        texto = request.GET.get('texto')

    return render(request, 'servico_register.html', {'form':form, 'erro':erro, 'texto':texto})

#Remover Serviço 

class ServicoDelete(DeleteView):
    model = Servico
    template_name = 'servico__confirm_delete.html'
    success_url = reverse_lazy('visualizartodosservios')

#visualizar serviços
@login_required
def visualiazer_servicos(request):
    visualizar_sd= ServicoFilter(request.GET, queryset=Servico.objects.all())
    return render(request, 'servico_view.html', {'ServicoFilter':visualizar_sd})


#preencher status automatico

@receiver(post_save, sender=Servico)
def preencher_formulario(sender, instance, **kwargs):
    if instance.Status == 'Fechamento':
        DemandaInterna.objects.create(
            Atividade=instance.Numero_Servico,  # Acessa o campo da instância atual
            tipo='',
            responsavel='',  
            status='Aguardando',
            data_solicitacao= datetime.now().date()  # Passa a data diretamente
        )


#pagina de serviços



def listar_servico_paginas(request):
    todos = Servico.objects.all()
    paginator = Paginator(todos, 2)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, 'servico_view.html', {'page_obj':page_obj})

#Update em Serviços

class ServicoUpdate(UpdateView):
    model = Servico
    template_name = 'servico_update.html'
    fields = ['Numero_Servico', 'PEP', 'Servico', 'Mês_servico', 'Ano_servico', 'data_da_solicitacao', 'Municipio', 'Endereco', 'Status','data_programacao', 'Valor_parcial', 'Valor_final', 'desenho_servico','foto_antes', 'foto_depois' , 'Observacao']
    success_url = reverse_lazy('visualizartodosservios')

class ServicoUpdateStatus(UpdateView):
    model = Servico
    template_name = 'servico_update.html'
    fields = ['Status']
    success_url = reverse_lazy('visualizartodosservios')

@login_required
def servico_update_servico(request, pk):
    servicos = get_object_or_404(Servico, pk=pk)
    contexto = {'servicos':servicos}
    return render(request, 'servico_update.html', contexto)

#visualiazar serviço unitario
@login_required
def servico_visualizar_com_id(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    contexto = {'servico':servico}
    return render(request, 'servico_unitario.html', contexto)

class ServicoView(DetailView):
    model = Servico
    template_name = 'servico_unitario.html'
    context_object_name = 'servico'


#contar serviço

def intem_lista(request):
    contar_andamento = Servico.objects.filter(Status='Andamento').count()
    contar_programacao = Servico.objects.filter(Status='Programação').count()
    contar_espera  = Servico.objects.filter(Status='Espera').count()
    Concluido = Servico.objects.filter(Status='Concluido').count()
    Fechamento = Servico.objects.filter(Status='Fechamento').count()
    Pagamento = Servico.objects.filter(Status='Pagamento').count()
    Recebido = Servico.objects.filter(Status='Recebido').count()


    context = {
        'contar_andamento':contar_andamento,
        'somar_andamento':Servico.somar_valor_status('Andamento'),
        'somar_programacao':Servico.somar_valor_status('Programação'),
        'somar_concluido':Servico.somar_valor_status('Concluido'),
        'somar_Fechamento':Servico.somar_valor_status('Fechamento'),
        'somar_Pagamento':Servico.somar_valor_status('Pagamento'),
        'somar_Espera':Servico.somar_valor_status_parcial('Espera'),
        'somar_Recebido':Servico.somar_valor_status('Recebido'),
        'contar_programacao':contar_programacao,
        'contar_espera':contar_espera,
        'Pagamento':Pagamento,
        'Concluido':Concluido,
        'Fechamento':Fechamento,
        'Recebido':Recebido,
    }
    return render(request, 'servico_dashboard.html', context)

#SOmar valores 

def somar_valor_status(request):
    somar_andamento = Servico.objects.filter(Status='Andamento').aggregate(valor_andamento=Sum('Valor_final'))

    context = {
        'valor_andamento':somar_andamento['valor_andamento'] or 0
    }

    return render(request, 'servico_dashboard.html', context)


#Demanda Internas

@login_required
def createdemanda(request):
    erro = None
    texto = None

    if request.method == 'POST':
        form = DemandaInternaform(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('Demandainternaviews')
    else:
        form = DemandaInternaform()
        erro = request.GET.get('erro')
        texto = request.GET.get('texto')
    
    return render(request, 'demanadainterna_criar.html', {'form':form, 'erro':erro, 'texto':texto})

#Update em demandas internas 


class DemandaUpdate(UpdateView):
    model = DemandaInterna
    template_name = 'demandainterna_update.html'
    form_class =DemandaInternaform
    #fields = ['Atividade', 'tipo', 'responsavel', 'status', 'data_solicitacao', 'data_conclusão', 'responsavel', 'arquivos', 'arquivos_complementar', 'arquivos_complementar1', 'arquivos_complementar2']
    success_url = reverse_lazy('Demandainternaviews')

@login_required
def demanda_interna_update(request, pk):
    demandas = get_object_or_404(DemandaInterna, pk=pk)
    contexto = {'demandas':demandas}
    return render(request, 'demandainterna_update.html', contexto)
#visualaizar todas

@login_required
def demandainternavisualizartd(request):
    demanda = DemandaFilter(request.GET, queryset= DemandaInterna.objects.all())
    return render(request, 'demandainterna_views.html', {'DemandaFilter':demanda})

#auterar status demanda interna

class DemandainternaStatus(UpdateView):
    model = DemandaInterna
    template_name = 'demandainterna_update.html'
    fields = ['status']
    success_url = reverse_lazy('Demandainternaviews')

#Remover Demanada Interna

class RemoverDemanda(DeleteView):
    model = DemandaInterna
    template_name = 'demanda__confirm_delete.html'
    success_url = reverse_lazy('Demandainternaviews')

#Banco de arquivos

@login_required
def CreateArquivos(request):
    erro = None
    texto = None

    if request.method == 'POST':
        form = BancoArquivoform(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('visualizararquivos')
    else:
        form = BancoArquivoform()
        erro = request.GET.get('erro')
        texto = request.GET.get('texto')
    
    return render(request, 'arquivos_criar.html', {'form':form, 'erro':erro, 'texto':texto})


@login_required
def visualizar_arquivos(request):
    arquivos =ArquivoFilter(request.GET, queryset= BancoArquivos.objects.all())
    return render(request, 'arquivos_visualizartd.html', {'ArquivoFilter':arquivos})


class ArquivoUodate(UpdateView):
    model = BancoArquivos
    template_name= 'arquivo_update.html'
    fields = ['EI_OC','tipo','municipio' ,'AS_Biult', 'Responsavel','Medicao', 'DWG', 'AES', 'ACOS']
    success_url = 'visualizararquivos'

@login_required
def atualizar_arquivos(request, pk):
    arquivos = get_object_or_404(BancoArquivos, pk=pk)
    contexto={'arquivos':arquivos}
    return render(request, 'arquivo_update.html', contexto)

#Arquivoviews


class ArquivoViews(DetailView):
    model = BancoArquivos
    template_name = 'arqvuivo_unitario.html'
    context_object_name = 'detalhe'

    def get_success_url(self):
        return reverse_lazy('#', kwargs={'pk':self.object.pk})

#filtro 

@login_required
def arquivo_filtro(request):
    filtro = BancoArquivos.objects.all()
    return render(request, 'arquivos_visualizartd.html', {'filtro':filtro})

#login


def logar(request):
    if request.user.is_authenticated:
        return redirect("")
    if request.method != "POST":
        return render(request, "login_teste.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("homapage")
    else:
        return HttpResponse("invalid credentials", status=401)
    return render(request, 'base.html')

#exportar execel colaborador

def exportar_para_execel_colaboradores(request):
    colaboradores_excel = collaborator.objects.all().values()
    df = pd.DataFrame(colaboradores_excel)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="colaboradores_excel.xlsx"'
    df.to_excel(response, index=False)
    return response

#exportar execel serviços 

def servico_exportar_execel(request):
    servico_execel = Servico.objects.all().values()
    df = pd.DataFrame(servico_execel)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="servico_excel.xlsx"'
    df.to_excel(response, index=False)
    return response

#exportar execel Demandas internas 

def demandainterna_exportar_execel(request):
    demandainterna_execel = Servico.objects.all().values()
    df = pd.DataFrame(demandainterna_execel)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="demandainterna_excel.xlsx"'
    df.to_excel(response, index=False)
    return response

def logout_view(request):
    logout(request)
    return redirect ("homapage")