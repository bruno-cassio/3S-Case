import graphene
from graphene_django import DjangoObjectType
from graphene.types.generic import GenericScalar
from .models import Auditoria


class AuditoriaType(DjangoObjectType):
    entrada = GenericScalar()
    saida = GenericScalar()

    class Meta:
        model = Auditoria
        fields = ("id", "modulo", "acao", "sucesso", "entrada", "saida", "criado_em")


class Query(graphene.ObjectType):
    auditorias = graphene.List(AuditoriaType)

    def resolve_auditorias(root, info):
        # Garantir que retorna algo iterável
        return Auditoria.objects.all().order_by("-criado_em")


schema = graphene.Schema(query=Query)
