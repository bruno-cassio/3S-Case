import pytest
import requests
import time
from django.conf import settings
from core.models import Auditoria


for i in range(10):
    try:
        r = requests.get("http://case3s-django:8001/api/questao/1/?texto=banana", timeout=3)
        print("✅ Django está respondendo!")
        break
    except Exception as e:
        print(f"⏳ Django ainda não respondeu... tentativa {i+1}/10")
        time.sleep(3)
else:
    pytest.fail("❌ Django não subiu após 30 segundos.")


@pytest.mark.django_db
def test_fluxo_questao_1_e_auditoria():
    """
    Testa o fluxo completo:
    Front (via Django API) → Django → FastAPI → Banco (Auditoria)
    """

    print("\n🚀 Iniciando teste de fluxo completo auditoria (questao_1)\n")

    # --- Passo 1: limpar auditorias anteriores ---
    Auditoria.objects.all().delete()
    print("🧹 Tabela Auditoria limpa antes do teste")

    # --- Passo 2: Executar a requisição Django /api/questao/1 ---
    url = "http://case3s-django:8001/api/questao/1/"
    params = {"texto": "banana"}
    print(f"🌐 Fazendo requisição para {url} com params={params}")

    try:
        response = requests.get(url, params=params, timeout=10)
        print(f"📡 Status code: {response.status_code}")
        print(f"📦 JSON retornado: {response.json()}")
    except Exception as e:
        pytest.fail(f"❌ Erro ao fazer requisição: {e}")

    # --- Passo 3: Aguardar e verificar se gerou auditoria ---
    time.sleep(2)
    total = Auditoria.objects.count()
    print(f"🔎 Total de registros na tabela Auditoria: {total}")

    if total == 0:
        print("⚠️ Nenhum registro de auditoria criado!")
        print("❌ Fluxo interrompido entre Django e FastAPI.")
        pytest.fail("Auditoria não foi registrada no banco.")

    # --- Passo 4: Exibir detalhes do registro ---
    registros = list(Auditoria.objects.values("id", "modulo", "acao", "sucesso", "entrada", "saida"))
    print("📘 Registros encontrados:")
    for reg in registros:
        print(reg)

    # --- Passo 5: Assert final ---
    assert total > 0, "Auditoria deveria ter sido criada"
    print("\n✅ Teste de fluxo completo finalizado com sucesso.\n")
