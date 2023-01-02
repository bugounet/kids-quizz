from django.shortcuts import render
from django.http.response import JsonResponse
from .models import QuestionReponse


# Create your views here.
def index(request):
    return render(request, "player/index.html")


def question_aleatoire(request):
    question = QuestionReponse.objects.filter(repondu=False).order_by("?").first()
    if not question:
        return JsonResponse({})
    QuestionReponse.objects.filter(id=question.id).update(repondu=True)
    return JsonResponse({
        "id": question.id,
        "enonce": question.enonce,
        "reponse": question.reponse,
        "repondu": False
    })
