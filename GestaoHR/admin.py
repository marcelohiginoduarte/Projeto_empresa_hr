from django.contrib import admin
from GestaoHR.models import collaborator, Aquivo, Servico, BancoArquivos, DemandaInterna, SESMT, ArquivoSesmt, arquivos_foto, FotosCampo

admin.site.register(collaborator)

class ListandoCollaborator(admin.ModelAdmin):
    list_display = ("Nome", "CPF", "RG")
    list_display_links = ("Nome", "CPF")

admin.site.register(Aquivo)

class ListandoArquivo(admin.ModelAdmin):
    list_display=('Nome', 'Arquivo_ponto')
    list_display_links = ('Nome', 'Arquivo_ponto')

admin.site.register(Servico)

class ListandoServico(admin.ModelAdmin):
    list_display = ('PEP', 'Municipio')
    list_display_links = ('PEP', 'Municipio')

admin.site.register(BancoArquivos)

class Listandobdarquivos(admin.ModelAdmin):
    list_display = ('EI_OC', 'municipio')
    list_display_links = ('EI_OC', 'municipio')

    admin.site.register(DemandaInterna)

class ListandoDemandaInterna(admin.ModelAdmin):
    list_display = ('Atividade', 'tipo')
    list_display_links = ('Atividade', 'tipo')

admin.site.register(SESMT)
class ListandoSESMT(admin.ModelAdmin):
    list_display = ('Atividade', 'tipo')
    list_display_links = ('Atividade', 'tipo')

admin.site.register(ArquivoSesmt)
class ArquivosLista(admin.ModelAdmin):
    list_display = ('Atividade', 'tipo')
    list_display_links = ('Atividade', 'tipo')

admin.site.register(arquivos_foto)
admin.site.register(FotosCampo)