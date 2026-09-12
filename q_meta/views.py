from django.shortcuts import render
from question.models import Question
from answer.models import Answer
from .models import Q_meta


def question_meta(request, slug):
    """
    Display the (meta) analyses for the :model:`question.Question`.

    :param request: The requested question.
    :param slug: The identification (slug) of the request.

    **Context**

    ``question_meta``
        An instance of :model:`question.Question` from :model:`answer.Answer`.

    **Template**

    :template:`question/question_detail.html`.
    """

    questions = Q_meta.objects.filter(question__slug=slug)

    context = {
        "questions": questions,
    }

    return render(
        request,
        "question/question_detail.html",
        context
    )
