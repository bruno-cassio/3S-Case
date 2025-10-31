FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app/api_fastapi

# Copiar e instalar dependências
COPY requirements.txt /app/api_fastapi/
RUN pip install --no-cache-dir -r /app/api_fastapi/requirements.txt

# Copiar o código
COPY . /app/api_fastapi/

# Adicionar o PYTHONPATH para reconhecer /app
ENV PYTHONPATH=/app

# Porta padrão
EXPOSE 8000

# Comando padrão
CMD ["uvicorn", "api_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
