set dotenv-load := true
set positional-arguments

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

foo:
  echo $0

admin-generator:
    {{dco-run}} {{manage}} admin_generator

up:
    docker-compose up -d filmer

logs:
    docker-compose logs -f filmer

start: up logs
