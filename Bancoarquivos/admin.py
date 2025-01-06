from django.contrib import admin
from Bancoarquivos.models import BancoArquivos


class Listandobdarquivos(admin.ModelAdmin):
    list_display = ("EI_OC", "municipio")
    list_display_links = ("EI_OC", "municipio")


admin.site.register(BancoArquivos, Listandobdarquivos)
