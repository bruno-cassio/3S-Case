from django.db import models

class Auditoria(models.Model):
    modulo = models.CharField(max_length=100)
    acao = models.CharField(max_length=50)
    entrada = models.JSONField()
    saida = models.JSONField(null=True, blank=True)
    sucesso = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.modulo} - {self.acao} ({'OK' if self.sucesso else 'FALHA'})"
