from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Conteudo(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    conteudo_html = models.TextField("conteúdo HTML")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Menu(models.Model):
    INTERNO = "interno"
    EXTERNO = "externo"
    TIPOS = [
        (INTERNO, "Conteúdo interno"),
        (EXTERNO, "Link externo"),
    ]

    titulo = models.CharField(max_length=50)
    tipo_destino = models.CharField(max_length=10, choices=TIPOS, default=INTERNO)
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    conteudo = models.ForeignKey(
        Conteudo, on_delete=models.SET_NULL, null=True, blank=True,
        help_text="Use quando o destino for Conteúdo interno.",
    )
    url_externa = models.URLField(
        blank=True, help_text="Use quando o destino for Link externo.",
    )

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        return self.titulo

    def clean(self):
        if self.tipo_destino == self.INTERNO and not self.conteudo:
            raise ValidationError("Escolha um conteúdo para o destino interno.")
        if self.tipo_destino == self.EXTERNO and not self.url_externa:
            raise ValidationError("Informe a URL para o link externo.")

    @property
    def link(self):
        if self.tipo_destino == self.INTERNO and self.conteudo:
            return reverse("portal:conteudo", args=[self.conteudo.slug])
        return self.url_externa

    @property
    def eh_externo(self):
        return self.tipo_destino == self.EXTERNO
