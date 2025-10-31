from fastapi import FastAPI
from api_fastapi.routers import questao1, questao2, questao3, questao4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Case Técnico 3S API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questao1.router, prefix="/questao/1", tags=["Questão 1"])
app.include_router(questao2.router, prefix="/questao/2", tags=["Questão 2"])
app.include_router(questao3.router, prefix="/questao/3", tags=["Questão 3"])
app.include_router(questao4.router, prefix="/questao/4", tags=["Questão 4"])

@app.get("/")
def root():
    return {"message": "API FastAPI do Case Técnico 3S rodando com sucesso!"}
