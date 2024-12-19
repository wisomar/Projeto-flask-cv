# Usar uma imagem base com Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o conteúdo do diretório local para o contêiner
COPY . /app

# Instalar dependências do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expôr a porta que o Flask usa
EXPOSE 5000

# Definir o comando para rodar a aplicação Flask
CMD ["python", "app/meu_site.py"]
