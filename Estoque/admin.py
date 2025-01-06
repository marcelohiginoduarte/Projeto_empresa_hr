from django.contrib import admin
from Estoque.models import Produto




class Produtoadmin(admin.ModelAdmin):
    list_display = ("nome", "codigo")


admin.site.register(Produto, Produtoadmin)
