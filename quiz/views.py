import random

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from quiz.models import Quiz
from quiz.serializers import QuizSerializer


@api_view(['GET'])
def helloAPI(request):
    return Response('ㅎㄴㅁㅁㄴㅇㄹ머ㅣㄴ어림널')

@api_view(['GET'])
def randomQuiz(request,id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs),id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)