from django.contrib import messages
from django.shortcuts import render
from .forms import AnswerNewTest, AnswerNewQuestion, AnswerNewAnswers
from .models import Answer


def test_answer_detail(request, slug):
    """
    Display all :model:`question.Question` per individual :model:`test.Test`.

    :param request: The requested test.
    :param slug: The identification (slug) of the request.
    """

    answers = Answer.objects.filter(test__slug=slug)

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
    Display the forms which create a new :model:`answer.Answer`.

    **Context**

    ``answer_new``
        An instance of :form:`answer.AnswerNewTest`, then :form:`answer.AnswerNewQuestion`, then :form:`answer.AnswerNewAnswers`.

    **Template**

    :template:`answer/answer_new.html`.
    """

    if request.method == "POST":
        answer_new_test = AnswerNewTest(data=request.POST)
        if answer_new_test.is_valid():
            answer_new_question = AnswerNewQuestion(data=request.POST)
            if answer_new_question.is_valid():
                answer_new_answers = AnswerNewAnswers(data=request.POST)

                answer_new_test.save()
                answer_new_question.save()
                answer_new_answers.save()

                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "New answer created"
                )

    answer = Answer()
    answer_new_test = AnswerNewTest()
    answer_new_question = AnswerNewQuestion()
    answer_new_answers = AnswerNewAnswers()

    context = {
        "answer": answer,
        "answer_new_test": answer_new_test,
        "answer_new_question": answer_new_question,
        "answer_new_answers": answer_new_answers
    }

    return render(
        request,
        "answer/answer_new.html",
        context
    )
