set dotenv-load := true



recipe-name:
    echo 'This is a recipe!'

# this is a comment
another-recipe:
    @echo 'This is another recipe.'

migrate:
    docker-compose run --rm filmer python manage.py migrate

up:
    docker-compose up -d filmer

logs:
    docker-compose logs -f filmer

start: up logs
