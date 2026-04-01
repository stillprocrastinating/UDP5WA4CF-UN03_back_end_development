from django.contrib import messages
from django.http import Http404
from django.shortcuts import render
from .forms import AnswerNew
from .models import Answer


def answer_detail_test(request, slug):
    """
    Display all :model:`question.Question` per individual :model:`test.Test`.

    :param request: The requested test.
    :param slug: The identification (slug) of the request.
    """

    answers = Answer.objects.filter(test__slug=slug)
    if not answers.exists():
        raise Http404

    context = {
        "answers": answers,
        "test": answers.first().test,
    }

    return render(
        request,
        "answer/test_answer_detail.html",
        context
    )


def answer_new(request):
    """
    Display the form which creates a new :model:`answer.Answer`.

    **Context**

    ``answer_new``
        An instance of :form:`answer.AnswerNew`.

    **Template**

    :template:`answer/answer_new.html`.
    """

    if request.method == "POST":
        answer_new = AnswerNew(data=request.POST)
        if answer_new.is_valid():
            answer_new.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "New answer created"
            )

    answer = Answer()
    answer_new = AnswerNew()

    context = {
        "answer": answer,
        "answer_new": answer_new
    }

    return render(
        request,
        "answer/answer_new.html",
        context
    )
