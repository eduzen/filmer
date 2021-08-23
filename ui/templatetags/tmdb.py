from django import template

register = template.Library()

@register.simple_tag
def show_movie(movie):
    print(vars(movie))
    return ""
    title = movie.get('title') or movie.get('name') or movie.get('original_title')

    if not title:
        title = "No title"
    print(movie)

    tag = f"<a href='{movie.get('imdb_link')}'>{title}</a>"
    return tag
