set dotenv-load := true
set positional-arguments

dco := "docker-compose"
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

remove-filmer:
  {{dco}} rm -sf filmer

restart: remove-filmer start

dockershell:
  {{dco-run}} bash

show-urls:
  {{dco-run}} {{manage}} show_urls

createsuperuser email:
  {{dco-run}} {{manage}} createsuperuser --email $1 --username $1

admin-generator appname:
  {{dco-run}} {{manage}} admin_generator $1

collectstatic:
  {{dco-run}} {{manage}} collectstatic --noinput

up:
  {{dco}} up -d filmer

logs:
  {{dco}} logs -f filmer

test params:
  {{dco-run}} pytest $1

new-secret-key:
  {{dco-run}} {{manage}} generate_secret_key

clean-python:
  #!/usr/bin/env python3
  import pathlib
  current_path = pathlib.Path(".").parent
  [p.unlink() for p in current_path.rglob('*.py[co]')]
  [p.rmdir() for p in current_path.rglob('__pycache__')]

start: up logs
