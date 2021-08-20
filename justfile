set dotenv-load := true

dco-run := "docker-compose run --rm filmer"
manage := "python manage.py"

default:
  @just --list

migrate:
    {{dco-run}} {{manage}} migrate

makemigrations:
    {{dco-run}} {{manage}} makemigrations

dbshell:
    {{dco-run}} {{manage}} dbshell

createsuperuser:
    {{dco-run}} {{manage}} createsuperuser

set positional-arguments
admin-generator appname:
  {{dco-run}} {{manage}} admin_generator $1

up:
    docker-compose up -d filmer

logs:
    docker-compose logs -f filmer

start: up logs
