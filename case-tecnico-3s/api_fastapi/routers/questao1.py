from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()


class Q1Response(BaseModel):
    texto_original: str
    texto_normalizado: str
    comeca_com_b: bool
    termina_com_a: bool
    resultado: bool
    detalhe: str

"""
Apenas um detalhe sobre minha decisão de desenvolvimento aqui, como o enunciado não especifica
se a verificação deve ser case sensitive ou não, optei por fazer uma verificação
não case sensitive. Nesse cenario atenderia, por exemplo, a presunção de o usuário 
desejar que a comparação não leve em conta letras maiúsculas ou minúsculas, a escolha de um produto 
em um Saas de comércio por exemplo (Banana, BANANA, bananA seriam atendidos permitindo autocomplete e busca em db).
Caso fosse um form de login por exemplo, aplicaria case sensitive.
"""

@router.get("/", response_model=Q1Response, summary="Verifica se começa com 'B' e termina com 'A' (sem case sensitive)")
def verificar_string(
    texto: str = Query(..., min_length=1, description="Texto a verificar; comparação não é case sensitive.")
):
    """
    Regra: texto deve **começar** com 'B' e **terminar** com 'A'.
    - Comparação não é case sensitive
    - Espaços nas pontas são ignorados
    """
    original = texto
    normalizado = texto.strip()
    upper = normalizado.upper()

    comeca = upper.startswith("B")
    termina = upper.endswith("A")
    ok = comeca and termina

    detalhe = (
        "Começa com 'B' e termina com 'A'." if ok
        else "Não atende à regra: precisa começar com 'B' e terminar com 'A'."
    )

    return Q1Response(
        texto_original=original,
        texto_normalizado=normalizado,
        comeca_com_b=comeca,
        termina_com_a=termina,
        resultado=ok,
        detalhe=detalhe,
    )
