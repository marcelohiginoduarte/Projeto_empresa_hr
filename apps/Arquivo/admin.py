from django.contrib import admin
from Arquivo.models import Aquivo

class ListandoArquivo(admin.ModelAdmin):
    list_display = ("Nome", "Arquivo_ponto")
    list_display_links = ("Nome", "Arquivo_ponto")


admin.site.register(Aquivo, ListandoArquivo)
