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

shell:
  {{dco-run}} {{manage}} shell_plus --print-sql

new-app appname:
  {{dco-run}} {{manage}} startapp $1

restart:
  docker-compose rm -sf filmer && docker-compose up -d filmer && docker-compose logs -f filmer

dockershell:
  {{dco-run}} bash

show-urls:
  {{dco-run}} {{manage}} show_urls

createsuperuser email:
  {{dco-run}} {{manage}} createsuperuser --email $1 --username $1

admin-generator appname:
  {{dco-run}} {{manage}} admin_generator $1

up:
  docker-compose up -d filmer

logs:
  docker-compose logs -f filmer

test:
  {{dco-run}} pytest -s

start: up logs
