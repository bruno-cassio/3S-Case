# Imagem base do Node
FROM node:20-alpine

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY package*.json ./

# Instala as dependências
RUN npm install

# Copia o restante do código do frontend
COPY . .

# Expõe a porta do servidor de desenvolvimento do Vite
EXPOSE 5173

# Comando para rodar o ambiente de desenvolvimento
CMD ["npm", "run", "dev", "--", "--host"]
