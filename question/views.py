from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Question


class QuestionList(generic.ListView):
    queryset = Question.objects.all()
