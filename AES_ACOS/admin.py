from django.contrib import admin
from AES_ACOS.models import AES_ACOS


class AESACOSadmin(admin.ModelAdmin):
    list_display = ("aes", "acos")
    list_display_links = ("aes", "acos")


admin.site.register(AES_ACOS, AESACOSadmin)
