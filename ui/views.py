from django.shortcuts import render
from django.http import HttpResponse

from tmdb import api

# def detail(request, poll_id):
#     try:
#         p = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404("Poll does not exist")
#     return render(request, 'polls/detail.html', {'poll': p})


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    trends = api.tmdb_trending_movies()
    return render(request, 'ui/base.html', {"trends": trends})
