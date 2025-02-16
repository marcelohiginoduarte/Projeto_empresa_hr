from django.contrib import admin
from Equipe.models import Equipe


class EquipeAdmin(admin.ModelAdmin):
    list_display = ("Codigo_Equipe", "Nome_encarregado")
    list_display_links = ("Codigo_Equipe", "Nome_encarregado")


admin.site.register(Equipe, EquipeAdmin)
