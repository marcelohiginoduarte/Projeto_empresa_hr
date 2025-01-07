from django.db import models

class AES_ACOS(models.Model):
    aes = models.FileField(upload_to="media/aes", blank=True, null=True)
    acos = models.FileField(upload_to="media/acos", blank=True, null=True)


