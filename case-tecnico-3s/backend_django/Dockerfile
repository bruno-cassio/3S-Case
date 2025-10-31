#imagem
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar e instalar dependências
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código
COPY . .

# Porta padrão
EXPOSE 8001

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
