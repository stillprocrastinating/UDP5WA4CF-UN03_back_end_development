from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Question


class QuestionList(generic.ListView):
    queryset = Question.objects.all()


def question_detail(request, slug):
    """
    Display an individual :model:`question.Question`.

    :param request: The requested question.
    :param slug: The identification (slug) of the request.
    """

    queryset = Question.objects.all()
    question = get_object_or_404(queryset, slug=slug)

    context = {
        "question": question,
    }

    return render(
        request,
        "question/question_detail.html",
        context,
    )
