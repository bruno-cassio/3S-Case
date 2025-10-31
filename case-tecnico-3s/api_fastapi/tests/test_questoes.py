from api_fastapi.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


# Questão 1 – Começa com B e termina com A
def test_q1_true_case_insensitive():
    r = client.get("/questao/1", params={"texto": "brunaA"})
    assert r.status_code == 200
    data = r.json()
    assert data["resultado"] is True
    assert data["comeca_com_b"] is True
    assert data["termina_com_a"] is True


def test_q1_false_case():
    r = client.get("/questao/1", params={"texto": "Anderson"})
    assert r.status_code == 200
    assert r.json()["resultado"] is False


# Questão 2 – Sequência aritmética (11,18,25,...)
def test_q2_primeiro_valor():
    r = client.get("/questao/2", params={"x": 1})
    assert r.status_code == 200
    assert r.json()["valor"] == 11


def test_q2_valores_medios():
    assert client.get("/questao/2", params={"x": 2}).json()["valor"] == 18
    assert client.get("/questao/2", params={"x": 200}).json()["valor"] == 1404
    assert client.get("/questao/2", params={"x": 254}).json()["valor"] == 1782


def test_q2_invalido_negativo():
    r = client.get("/questao/2", params={"x": 0})
    assert r.status_code == 422  # validação automática do FastAPI (gt=0)


# Questão 3 – Jogo de tabuleiro
def test_q3_min_turnos_probabilidade_e_combinacoes():
    r = client.get("/questao/3", params={"casas": 10})
    assert r.status_code == 200
    data = r.json()
    assert data["min_turnos"] == 4
    # probabilidade deve ser aproximadamente (1/3)**4 = 0.0123456
    assert abs(data["probabilidade_otima"] - 0.0123456) < 1e-5
    assert data["combinacoes_sem_loop"] == 274


def test_q3_invalido_menor_que_3():
    r = client.get("/questao/3", params={"casas": 2})
    assert r.status_code == 422  # ge=3 na validação


# Questão 4 – Férias e 13º proporcionais
def test_q4_proporcionalidades_basicas():
    r = client.get(
        "/questao/4",
        params={
            "data_admissao": "2023-03-10",
            "data_demissao": "2025-10-29"
        }
    )
    assert r.status_code == 200
    data = r.json()
    assert data["meses_ferias"] == 7
    assert data["meses_decimo"] == 10
    # proporções devem bater
    assert abs(data["proporcao_ferias"] - 7/12) < 1e-4
    assert abs(data["proporcao_decimo"] - 10/12) < 1e-4


def test_q4_data_invalida():
    r = client.get(
        "/questao/4",
        params={
            "data_admissao": "2025-10-29",
            "data_demissao": "2023-10-29"
        }
    )
    # FastAPI converte ValueError em 422
    assert r.status_code in (400, 422)
