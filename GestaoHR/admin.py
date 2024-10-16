from django.contrib import admin
from GestaoHR.models import collaborator, Aquivo, Servico, BancoArquivos, DemandaInterna, SESMT, ArquivoSesmt, arquivos_foto, FotosCampo, Produto
from django.core.exceptions import PermissionDenied


class ListandoCollaborator(admin.ModelAdmin):
    list_display = ("Nome", "CPF", "RG")
    search_fields = ("Nome",)
    list_display_links = ("Nome", "CPF")

admin.site.register(collaborator, ListandoCollaborator)



class ListandoArquivo(admin.ModelAdmin):
    list_display=('Nome', 'Arquivo_ponto')
    list_display_links = ('Nome', 'Arquivo_ponto')

admin.site.register(Aquivo, ListandoArquivo) 



class ListandoServico(admin.ModelAdmin):
    list_display = ('PEP', 'Municipio')
    list_display_links = ('PEP', 'Municipio')

admin.site.register(Servico, ListandoServico)



class Listandobdarquivos(admin.ModelAdmin):
    list_display = ('EI_OC', 'municipio')
    list_display_links = ('EI_OC', 'municipio')

admin.site.register(BancoArquivos, Listandobdarquivos)



class ListandoDemandaInterna(admin.ModelAdmin):
    list_display = ('Atividade', 'tipo')
    list_display_links = ('Atividade', 'tipo')

admin.site.register(DemandaInterna, ListandoDemandaInterna)


class ListandoSESMT(admin.ModelAdmin):
    list_display = ('Ultima_atualização', 'Ultima_atualização')
    list_display_links = ('Ultima_atualização', 'Ultima_atualização')

admin.site.register(SESMT, ListandoSESMT)


class ArquivosLista(admin.ModelAdmin):
    list_display = ('Nome', 'data_envio')
    list_display_links = ('Nome', 'data_envio')

admin.site.register(ArquivoSesmt, ArquivosLista)

class arquivofotocampo(admin.ModelAdmin):
    list_display = ('projeto',)
    list_display_links = ('projeto',)

admin.site.register(arquivos_foto, arquivofotocampo)

class fotoadmin(admin.ModelAdmin):
    list_display = ('projeto',)
    list_display_links = ('projeto',)

admin.site.register(FotosCampo, fotoadmin)

class Produtoadmin(admin.ModelAdmin):
    list_display = ('nome','codigo')

admin.site.register(Produto, Produtoadmin)