# 🚀 Case Técnico 3S — Fullstack Dockerized

Projeto fullstack com **Django + FastAPI + React + PostgreSQL**, totalmente orquestrado via **Docker Compose**.
A aplicação demonstra integração entre múltiplos serviços e registra automaticamente auditorias de chamadas de API no banco de dados.

---

## 🧩 Arquitetura Geral

```
[React Frontend] → [Django Backend] → [FastAPI API] → [PostgreSQL DB]
                           ↓
                       [GraphQL Auditoria]
```

- **Frontend (React + Vite)** — Interface para execução das 4 questões e visualização de auditoria.
- **Django** — Backend central que recebe requisições, chama a API FastAPI e grava logs no banco.
- **FastAPI** — Camada de serviços que processa as lógicas das questões.
- **PostgreSQL** — Banco de dados persistente, armazenando logs de auditoria.

---

## ⚙️ 1. Preparando o ambiente

1️⃣ Clone o repositório:

```bash
git clone https://github.com/seuusuario/3s-Case.git
cd 3s-Case/case-tecnico-3s
```

2️⃣ Certifique-se de ter o **Docker** e **Docker Compose** instalados.

---

## 🐳 2. Build e inicialização

A partir da **raiz do projeto**, rode:

```bash
docker compose up --build
```

O Docker criará as imagens e iniciará automaticamente os quatro containers:

- `case3s-django` — backend Django
- `case3s-fastapi` — API FastAPI
- `case3s-frontend` — interface React
- `case3s_db` — banco PostgreSQL

Após a build:

```
✅ Migrations aplicadas com sucesso.
VITE v5 ready on http://localhost:5173
```

---

## 🌐 3. Acessando a aplicação

- **Frontend (interface principal):** http://localhost:5173
- **Django (backend + auditoria):**  http://localhost:8001
- **FastAPI (documentação automática):**
   http://localhost:8000/docs

---

##  4. Tela de Requisições

Na tela inicial, há 4 **questões** demonstrando diferentes endpoints da API:

| Questão | Descrição                                                        | Endpoint           |
| -------- | ------------------------------------------------------------------ | ------------------ |
| 1        | Verifica se texto começa com**B** e termina com **A** | `/api/questao/1` |
| 2        | Gera e valida sequência numérica                                 | `/api/questao/2` |
| 3        | Calcula probabilidades e combinações                             | `/api/questao/3` |
| 4        | Calcula férias e 13º proporcional                                | `/api/questao/4` |

Ao executar qualquer questão, o Django chama a FastAPI, grava o log da operação no banco e retorna o resultado.

---

## 🧾 5. Tela de Auditoria

A aba **“Auditoria”** exibe todos os registros persistidos no banco:

- **Módulo:** nome da questão executada
- **Ação:** método HTTP (ex: GET)
- **Sucesso:** ✅ ou ❌ indicando o status

Esses registros vêm da tabela `core_auditoria` do PostgreSQL, acessada via **GraphQL**:

```
POST /graphql/
query { auditorias { modulo acao sucesso criado_em } }
```

---

## 🧹 6. Parar e limpar containers

Para encerrar tudo:

```bash
docker compose down -v
```

---

## 🧠 Observações

- Todas as variáveis sensíveis (DB, portas, URLs) estão configuradas no `.env` e no `docker-compose.yml`.
- O frontend consome o backend via `VITE_API_URL=http://localhost:8001/api`.
- O backend Django chama a FastAPI internamente via `case3s-fastapi:8000`.

---

## 👨‍💻 Autor

**Bruno Cássio Chiaca**
