from answer.models import Answer
from answer.views import test_answer_detail
from django.contrib import messages
# from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .forms import TestNew
from .models import Test


class TestList(generic.ListView):
    queryset = Test.objects.all().order_by("-date")
    paginate_by = 9


def test_detail(request, slug):
    """
    Display an individual :model:`test.Test`.

    :param request: The requested test.
    :param slug: The identification (slug) of the request.
    """

    queryset = Test.objects.all()
    test = get_object_or_404(queryset, slug=slug)

    context = {
        "test": test
    }

    return render(
        request,
        "test/test_detail.html",
        context
    )


def test_detail_page(request, slug):
    """
    Display the complete test_detail.html page using test_detail() and answer.test_answer_detail().

    :param request: The requested test.
    :param slug: The identification (slug) of the request.
    """

    answers = Answer.objects.filter(test__slug=slug)
    if answers.exists():
        return test_answer_detail(request, slug)

    return test_detail(request, slug)


def test_new(request):
    """
    Display the form which creates a new :model:`test.Test`.

    **Context**

    ``test_new``
        An instance of :form:`test.TestNew`.

    **Template**

    :template:`test/test_new.html`.
    """

    if request.method == "POST":
        test_new = TestNew(data=request.POST)
        if test_new.is_valid():
            test_new.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "New test created"
            )

    test = Test()
    test_new = TestNew()

    context = {
        "test": test,
        "test_new": test_new
    }

    return render(
        request,
        "test/test_new.html",
        context
    )
