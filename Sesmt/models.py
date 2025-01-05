from django.db import models


class SESMT(models.Model):
    Brigada_emergerncia = models.FileField(
        upload_to="media/sesmt/brigada", blank=True, null=True
    )
    CIPA = models.FileField(upload_to="media/sesmt/cipa", blank=True, null=True)
    CNPJ_CRB = models.FileField(upload_to="media/sesmt/cnpj", blank=True, null=True)
    CRB = models.FileField(upload_to="media/sesmt/crb", blank=True, null=True)
    Documentacao_veiculo = models.FileField(
        upload_to="media/sesmt/documentoveiculo", blank=True, null=True
    )
    manual_veiculo = models.FileField(
        upload_to="media/sesmt/manual", blank=True, null=True
    )
    orcamentos = models.FileField(
        upload_to="media/sesmt/orcamento", blank=True, null=True
    )
    PCSMO = models.FileField(upload_to="media/sesmt/pcsmo", blank=True, null=True)
    prg = models.FileField(upload_to="media/sesmt/prg", blank=True, null=True)
    plano_de_atendimento_emergencia = models.FileField(
        upload_to="media/sesmt/planodeatendimento", blank=True, null=True
    )
    plano_de_manutencao_frota = models.FileField(
        upload_to="media/sesmt/plfrota", blank=True, null=True
    )
    POP_lM_construcao = models.FileField(
        upload_to="media/sesmt/POPLMCONST", blank=True, null=True
    )
    POP_LV_contrucao = models.FileField(
        upload_to="media/sesmt/POPLVCONST", blank=True, null=True
    )
    POP_sesmt = models.FileField(
        upload_to="media/sesmt/POPSESMT", blank=True, null=True
    )
    PPCI = models.FileField(upload_to="media/sesmt/PPCI", blank=True, null=True)
    SESMT_t = models.FileField(upload_to="media/sesmt/sesmt_t", blank=True, null=True)
    Ultima_atualização = models.CharField(max_length=50)


class ArquivoSesmt(models.Model):
    Nome = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to="media/sesmt/sesmt_t")
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nome


class Document(models.Model):
    file = models.FileField(upload_to="documents/")
    version = models.PositiveIntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-updated_at"]
        constraints = [
            models.UniqueConstraint(fields=["file", "version"], name="unique_file_version")
        ]

    def __str__(self):
        return f"{self.file.name} (v{self.version})"

    def save(self, *args, **kwargs):
        if not self.pk:
            # Increment the version if the file already exists
            latest_doc = Document.objects.filter(file=self.file).order_by("-version").first()
            if latest_doc:
                self.version = latest_doc.version + 1
        super().save(*args, **kwargs)
