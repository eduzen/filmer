from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tmdb import api


@login_required
def index(request):
    trends = api.tmdb_trending_movies()
    return render(request, "ui/base.html", {"trends": trends})
