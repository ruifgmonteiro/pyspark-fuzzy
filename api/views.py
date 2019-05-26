from django.http import HttpResponse
from api.fuzzy_matcher import get_similar_entities
from django.http import JsonResponse
import json


def index(request):
    return HttpResponse("Hello, world. You're at the fuzzy index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def test(request, company_id):
    data = get_similar_entities(company_id)
    return JsonResponse(data, safe=False)