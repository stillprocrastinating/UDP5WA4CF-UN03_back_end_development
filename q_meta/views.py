from django.shortcuts import render
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

    q_metas = Q_meta.objects.filter(question__slug=slug)

    context = {
        "q_metas": q_metas,
        "question": q_metas.first().question,
    }

    return render(
        request,
        "q_meta/q_meta_detail.html",
        context
    )
