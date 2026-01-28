from django.shortcuts import render
from django.views import generic
from .models import Test


class TestList(generic.ListView):
    queryset = Test.objects.all()
    paginate_by = 12
