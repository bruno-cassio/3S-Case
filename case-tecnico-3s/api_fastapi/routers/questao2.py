from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()

A1 = 11  # primeiro termo
R = 7    # razão da PA


class Q2Response(BaseModel):
    posicao: int
    valor: int
    formula: str
    demonstracao: str
    primeiro_termo: int
    razao: int


@router.get("/", response_model=Q2Response, summary="Valor na posição x da sequência 11,18,25,... (PA, r=7)")
def valor_sequencia(
    x: int = Query(..., gt=0, description="Posição na sequência (inicia em 1).")
):
    """
    Sequência aritmética com:
    - Primeiro termo a1 = 11 (conforme o enunciado denotou a sequencia 11, 18, 25, 32, 39... como base )
    - Razão r = 7 (jumps do fluxo)
    Fórmula: a_n = 11 + (n - 1) * 7
    """
    valor = A1 + (x - 1) * R
    formula = f"a_n = {A1} + (n - 1) * {R}"
    demonstracao = f"Para n={x}: {A1} + ({x} - 1) * {R} = {valor}"

    return Q2Response(
        posicao=x,
        valor=valor,
        formula=formula,
        demonstracao=demonstracao,
        primeiro_termo=A1,
        razao=R,
    )
