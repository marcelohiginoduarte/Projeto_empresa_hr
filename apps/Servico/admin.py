from django.contrib import admin
from .models import Servico


class ListandoServico(admin.ModelAdmin):
    list_display = ("PEP", "Municipio")
    list_display_links = ("PEP", "Municipio")


admin.site.register(Servico, ListandoServico)


