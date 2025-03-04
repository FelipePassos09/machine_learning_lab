# Usa a imagem oficial do PostgreSQL
FROM postgres:latest

# Define a senha padrão do PostgreSQL (altere conforme necessário)
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=hunter09
ENV POSTGRES_DB=main_database

# Expõe a porta 5432 dentro do contêiner (não muda no container, só no host)
EXPOSE 5432

# Comando de inicialização do PostgreSQL
CMD ["postgres"]