from django.contrib import admin
from demandainterna.models import DemandaInterna


class ListandoDemandaInterna(admin.ModelAdmin):
    list_display = ("Atividade", "tipo")
    list_display_links = ("Atividade", "tipo")


admin.site.register(DemandaInterna, ListandoDemandaInterna)

