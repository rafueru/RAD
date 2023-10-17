# Defina a imagem base
FROM python:3.9-slim

# Instale as dependências necessárias para o tkinter
RUN apt-get update && apt-get install -y tk && rm -rf /var/lib/apt/lists/*

# Demais comandos do seu Dockerfile
WORKDIR /app
# Instalando dependências
RUN pip install requests
COPY . .
RUN chmod +x frontend.py
CMD ["python", "frontend.py"]
