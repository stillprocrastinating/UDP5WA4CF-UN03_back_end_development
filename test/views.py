from django.shortcuts import render
from django.views import generic
from .models import Test


class TestList(generic.ListView):
    queryset = Test.objects.all().order_by("-date")
    paginate_by = 12


#def test_new(request):
#    """
#    Display the form which creates a new test.
#    """
