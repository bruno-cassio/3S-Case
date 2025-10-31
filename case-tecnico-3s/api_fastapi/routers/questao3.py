from fastapi import APIRouter, Query
from pydantic import BaseModel
import math

router = APIRouter()

"""
Esta questão é a de maior complexidade no teste, quebrei as funções auxiliares afim de facilitar a leitura
e, por obvio, a separação de responsabilidades. Assim mantenho o mesmo padrão das outras questões e
estrutura do teste centralizado em FastAPI.
No entanto, se tratando de um módulo com similaridade em cruzamento de regras, cálculo e ingestão de dependências
eu trataria as funções auxiliares em um módulo (Classes) separado, para manter o router (ou uma View no Django)
mais limpo e focado apenas na orquestração.

"""

# ----------MODELO DE RESPOSTA ----------
class Q3Response(BaseModel):
    casas: int
    min_turnos: int
    probabilidade_otima: float
    probabilidade_formatada: str
    combinacoes_sem_loop: int
    explicacao: str


# ----------FUNÇÕES AUXILIARES ---------- ()

def calcular_min_turnos(casas: int) -> int:
    """
    Caminho ótimo = sempre andar o máximo possível (3 casas por turno)
    Fórmula: ceil(casas / 3)
    """
    return math.ceil(casas / 3)


def calcular_probabilidade_otima(turnos: int) -> float:
    """
    Cada jogada tem 3 resultados possíveis (1, 2, 3).
    A chance de tirar exatamente a sequência ótima em 'turnos' jogadas
    é (1/3)^turnos.
    """
    return (1 / 3) ** turnos


def contar_combinacoes_sem_loop(casas: int) -> int:
    """
    Conta quantas sequências possíveis de passos (1,2,3)
    somam exatamente 'casas' sem ultrapassar o limite (sem looping).

    Essa é uma variação do problema clássico:
    "De quantas maneiras posso subir uma escada de N degraus
    pulando 1, 2 ou 3 degraus por vez?"
    → Solução por programação dinâmica.
    """
    if casas < 0:
        return 0
    dp = [0] * (casas + 1)
    dp[0] = 1  # base: 1 forma de ficar parado (soma 0)

    for i in range(1, casas + 1):
        dp[i] += dp[i - 1] if i - 1 >= 0 else 0
        dp[i] += dp[i - 2] if i - 2 >= 0 else 0
        dp[i] += dp[i - 3] if i - 3 >= 0 else 0

    return dp[casas]


# ----------ENDPOINT PRINCIPAL ----------
@router.get("/", response_model=Q3Response, summary="Simulação do jogo de tabuleiro (roleta 1–3 casas)")
def jogo_tabuleiro(
    casas: int = Query(..., ge=3, description="Número de casas do tabuleiro (mínimo = 3)."),
):
    """
    Simula um jogo com tabuleiro unidirecional.

    Regras:
    - Jogador anda 1, 2 ou 3 casas (ruim, bom, ótimo) por turno (sorteio aleatório);
    - Se o número sorteado excede as casas restantes, ele 'loopa' e reinicia (ou seja ultima casa + excedente);
    - O objetivo é alcançar a última casa no menor número de turnos possível.

    Retorna:
    1️⃣ Mínimo de turnos para vencer (caminho ótimo);
    2️⃣ Probabilidade de executar exatamente esse caminho;
    3️⃣ Número de combinações possíveis de movimentos sem looping.
    """

    #Caminho ótimo
    min_turnos = calcular_min_turnos(casas)

    #Probabilidade do caminho ótimo
    prob_otima = calcular_probabilidade_otima(min_turnos)
    prob_formatada = f"{prob_otima * 100:.5f}%"

    #Combinações sem looping (DP)
    combinacoes = contar_combinacoes_sem_loop(casas)

    #Retorno string amigável para eu poder puxar no front, menos trabalho no react pra resp.
    explicacao = (
        f"O tabuleiro possui {casas} casas. "
        f"O caminho ótimo exige {min_turnos} turnos (andando 3 casas por jogada). "
        f"A probabilidade de executar essa sequência perfeita é {prob_formatada}. "
        f"Existem {combinacoes} combinações de movimentos possíveis sem looping."
    )

    return Q3Response(
        casas=casas,
        min_turnos=min_turnos,
        probabilidade_otima=prob_otima,
        probabilidade_formatada=prob_formatada,
        combinacoes_sem_loop=combinacoes,
        explicacao=explicacao,
    )
