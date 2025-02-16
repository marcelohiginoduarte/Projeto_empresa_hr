from django.contrib import admin
from Fotoscampo.models import FotosCampo

class fotoadmin(admin.ModelAdmin):
    list_display = ("projeto",)
    list_display_links = ("projeto",)


admin.site.register(FotosCampo, fotoadmin)
