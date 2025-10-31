from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from .views import QuestaoView
from .schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/questao/<int:numero>/", QuestaoView.as_view(), name="questao"),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
