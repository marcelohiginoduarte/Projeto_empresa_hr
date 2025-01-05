from django.contrib import admin
from Sesmt.models import SESMT, ArquivoSesmt

class ListandoSESMT(admin.ModelAdmin):
    list_display = ("Ultima_atualização", "Ultima_atualização")
    list_display_links = ("Ultima_atualização", "Ultima_atualização")


admin.site.register(SESMT, ListandoSESMT)


class ArquivosLista(admin.ModelAdmin):
    list_display = ("Nome", "data_envio")
    list_display_links = ("Nome", "data_envio")


admin.site.register(ArquivoSesmt, ArquivosLista)
