from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import QuizSerializer
from django.contrib import messages

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
  if quiz:
    if id == 10: id = 12
    now_quiz = list(Quiz.objects.filter(id=id).values('score'))
    id += 1
    now_score = now_quiz[0]['score'].split("/")[int(quiz)]
    if id == 2:
      select = Select.objects.create(score=now_score)
      select_id = select.id
    else:
      select = get_object_or_404(Select, pk=select_id)
      select.score += int(now_score)
      select.save()
    if id == 13:
      return redirect('quiz:resultQuiz', select_id)
    else:
      return redirect('quiz:selectQuiz', select_id, id)
  messages.warning(request, "적어도 하나의 답변을 선택해주세요.")
  return render(request, 'quiz.html', {'select_id': select_id, 'id' : id})

def resultQuiz(request, select_id):
  select = get_object_or_404(Select, pk=select_id)
  for result_id in range(1, 5):
    result_high = get_object_or_404(Result, pk=result_id)
    result_low = get_object_or_404(Result, pk=result_id+1)
    context = {
      'select' : select,
      'result' : result_low
    }
    
    if result_low.result_score < select.score < result_high.result_score:
      return render(request, 'quiz_result.html', context)
    elif select.score <= 69:
      result_low = get_object_or_404(Result, pk=5)
      context = {
        'select' : select,
        'result' : result_low
      }
      return render(request, 'quiz_result.html', context)