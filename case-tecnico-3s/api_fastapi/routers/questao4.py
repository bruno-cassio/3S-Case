from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from datetime import date

router = APIRouter()

class Q4Response(BaseModel):
    meses_ferias: int
    meses_decimo: int
    proporcao_ferias: float
    proporcao_decimo: float
    valor_ferias: float
    valor_decimo: float
    total_a_receber: float
    explicacao: str


@router.get("/", response_model=Q4Response, summary="Cálculo proporcional de Férias e 13º (com base salarial)")
def calcular_beneficios(
    data_admissao: date = Query(..., description="Data de admissão (YYYY-MM-DD)"),
    data_demissao: date = Query(..., description="Data de demissão (YYYY-MM-DD)"),
    salario_base: float = Query(..., description="Salário base mensal em reais")
):
    """
    Calcula o valor proporcional de Férias e 13º salário,
    com base nas datas e no salário informado.
    """

    if data_demissao < data_admissao:
        raise HTTPException(status_code=400, detail="A data de demissão não pode ser anterior à de admissão.")

    # --- Férias ---
    anos_completos = data_demissao.year - data_admissao.year
    aniversario_atual = date(data_admissao.year + anos_completos, data_admissao.month, data_admissao.day)
    if aniversario_atual > data_demissao:
        aniversario_atual = date(data_admissao.year + anos_completos - 1, data_admissao.month, data_admissao.day)
    meses_ferias = (data_demissao.year - aniversario_atual.year) * 12 + (data_demissao.month - aniversario_atual.month)
    meses_ferias = max(0, min(12, meses_ferias))
    proporcao_ferias = round(meses_ferias / 12, 4)

    # --- 13º ---
    meses_decimo = data_demissao.month
    proporcao_decimo = round(meses_decimo / 12, 4)

    # --- Cálculos monetários / multiplicando o salario base pelo beneficio proporcional ---
    valor_ferias = round(salario_base * proporcao_ferias, 2)
    valor_decimo = round(salario_base * proporcao_decimo, 2)
    total = round(valor_ferias + valor_decimo, 2)

    explicacao = (
        f"Entre {data_admissao.strftime('%d/%m/%Y')} e {data_demissao.strftime('%d/%m/%Y')}, "
        f"o funcionário acumulou {meses_ferias} mês(es) proporcionais de férias ({proporcao_ferias:.2%}) "
        f"e {meses_decimo} mês(es) de 13º salário ({proporcao_decimo:.2%}). "
        f"Com um salário base de R$ {salario_base:,.2f}, "
        f"tem direito a R$ {valor_ferias:,.2f} de férias e R$ {valor_decimo:,.2f} de 13º, "
        f"totalizando R$ {total:,.2f}."
    )

    return Q4Response(
        meses_ferias=meses_ferias,
        meses_decimo=meses_decimo,
        proporcao_ferias=proporcao_ferias,
        proporcao_decimo=proporcao_decimo,
        valor_ferias=valor_ferias,
        valor_decimo=valor_decimo,
        total_a_receber=total,
        explicacao=explicacao
    )
