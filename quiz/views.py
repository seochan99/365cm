from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import QuizSerializer

@api_view(['GET'])
def viewQuiz(request, id):
  totalQuizs = list(Quiz.objects.filter(id=id))
  serializer = QuizSerializer(totalQuizs, many=True)
  return Response(serializer.data)

def mainQuiz(request):
  return render(request, 'quiz_main.html')

def selectQuiz(request, select_id, id):
  return render(request, 'quiz.html', {'select_id': select_id, 'id' : id})

def nextQuiz(request, select_id, id):
  quiz = request.POST.get('quiz')
  if id == 10: id = 12
  now_quiz = list(Quiz.objects.filter(id=id).values('score'))
  id += 1
  now_score = now_quiz[0]['score'].split("/")[int(quiz)]
  if id == 2:
    select = Select.objects.create(user=request.user, score=now_score)
    select_id = select.id
  else:
    select = get_object_or_404(Select, pk=select_id)
    select.score += int(now_score)
    select.save()
  if id == 13:
    return render(request, 'quiz_result.html', { 'select' : select })
  else:
    return redirect('quiz:selectQuiz', select_id, id)
