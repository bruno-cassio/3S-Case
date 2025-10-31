import pytest
from django.urls import reverse
from django.test import Client
from core.models import Auditoria

pytestmark = pytest.mark.django_db

@pytest.fixture
def client():
    return Client()

"""
Minha aplicação de testes automatizados para este back em Django  valida o comportamento do backend,
cobrindo tanto testes unitários quanto de integração, executados automaticamente durante o build do Docker.

  Teste unitário / controlado
      - A função `test_comunicacao_com_fastapi` utiliza `monkeypatch` para substituir a função `requests.get`
        e simular a resposta da API FastAPI.
      - Assim, garante que rotas, views e models interagem corretamente.

  Teste de integração completo
      - A função `test_graphql_listagem_auditoria` insere registros reais no banco (ORM)
        e executa uma query GraphQL simulando uma requisição real do cliente.
      - Valida a integração entre as camadas: banco de dados, schema Graphene e camada HTTP do Django.
      - Comprova que o backend responde adequadamente às consultas, retornando dados consistentes.
"""

def test_comunicacao_com_fastapi(client, monkeypatch):
    """
    Simula a chamada do endpoint /api/questao/2 e valida se:
      - A resposta foi retornada (mockada)
      - Um registro foi criado na tabela Auditoria
    """

    # Mock do .get dentro da view
    def mock_get(url, params=None, **kwargs):
        class MockResponse:
            status_code = 200

            def json(self):
                return {"resultado": "ok", "questao": url}

            def raise_for_status(self):
                return None

        return MockResponse()


    import core.views as views
    monkeypatch.setattr(views.requests, "get", mock_get)

    response = client.get(reverse("questao", args=[2]), {"x": 5})
    assert response.status_code == 200
    data = response.json()
    assert data["resultado"] == "ok"

    audit = Auditoria.objects.first()
    assert audit is not None
    assert audit.modulo == "questao_2"
    assert audit.sucesso is True


def test_graphql_listagem_auditoria(client):
    """
    Valida se o endpoint /graphql responde e traz auditorias registradas.
    """
    Auditoria.objects.create(
        modulo="questao_1",
        acao="GET",
        entrada={"x": 1},
        saida={"resultado": "ok"},
        sucesso=True,
    )

    query = """
    {
      auditorias {
        modulo
        acao
        sucesso
      }
    }
    """
    response = client.post("/graphql/", data={"query": query}, content_type="application/json")
    assert response.status_code == 200
    content = response.json()
    data = content.get("data", {}).get("auditorias", [])
    assert len(data) >= 1
    assert data[0]["modulo"] == "questao_1"
