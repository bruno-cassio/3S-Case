from django.contrib import admin
from .models import Auditoria

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ("modulo", "acao", "sucesso", "criado_em")
    search_fields = ("modulo", "acao")
    list_filter = ("sucesso",)
