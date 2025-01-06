from django.contrib import admin
from GestaoHR.models import (
    collaborator,
    arquivos_foto,
    AES_ACOS,
    Caderno_servico,
)


class ListandoCollaborator(admin.ModelAdmin):
    list_display = ("Nome", "CPF", "RG")
    search_fields = ("Nome",)
    list_display_links = ("Nome", "CPF")


admin.site.register(collaborator, ListandoCollaborator)


class arquivofotocampo(admin.ModelAdmin):
    list_display = ("projeto",)
    list_display_links = ("projeto",)


admin.site.register(arquivos_foto, arquivofotocampo)


class AESACOSadmin(admin.ModelAdmin):
    list_display = ("aes", "acos")
    list_display_links = ("aes", "acos")


admin.site.register(AES_ACOS, AESACOSadmin)


class Caderno_servicoadmin(admin.ModelAdmin):
    list_display = ("nome",)
    list_display_links = ("nome",)


admin.site.register(Caderno_servico, Caderno_servicoadmin)



