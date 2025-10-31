import requests
from django.http import JsonResponse
from django.views import View
from .models import Auditoria
from django.db import IntegrityError, OperationalError

FASTAPI_BASE_URL = "http://case3s-fastapi:8000"


class QuestaoView(View):
    """
    View responsável por intermediar as requisições entre o Django e a API FastAPI,
    registrando automaticamente auditoria de execução no banco.
    """

    def get(self, request, numero):
        params = request.GET.dict()
        url = f"{FASTAPI_BASE_URL}/questao/{numero}"

        try:
            # --- Chama a FastAPI ---
            response = requests.get(url, params=params, timeout=10)
            if response.status_code >= 500:
                raise requests.exceptions.RequestException(f"FastAPI retornou {response.status_code}")

            response.raise_for_status()
            data = response.json()

            # --- Registra sucesso na auditoria ---
            try:
                audit = Auditoria.objects.create(
                    modulo=f"questao_{numero}",
                    acao="GET",
                    entrada=params,
                    saida=data,
                    sucesso=True,
                )
                print(f"✅ Auditoria registrada: ID={audit.id} | modulo={audit.modulo} | sucesso={audit.sucesso}", flush=True)

            except (IntegrityError, OperationalError) as db_err:
                print(f"❌ ERRO AO SALVAR AUDITORIA: {db_err}", flush=True)


            return JsonResponse(data, status=200)

        except requests.exceptions.RequestException as e:
            # Erros de rede / timeout
            erro_msg = f"Erro de comunicação com FastAPI: {str(e)}"

        except Exception as e:
            # Qualquer outro erro (ex: ValueError, JSON decode etc)
            import traceback

            erro_msg = f"Erro interno: {str(e)}"
            traceback.print_exc()
            erro_msg = f"Erro interno: {str(e)}"

        # --- Em caso de erro, registra tentativa com sucesso=False ---
        Auditoria.objects.create(
            modulo=f"questao_{numero}",
            acao="GET",
            entrada=params,
            saida={"erro": erro_msg},
            sucesso=False,
        )

        return JsonResponse({"erro": erro_msg}, status=500)
