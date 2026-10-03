from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from .forms import AnswerForm
from .models import Answer


def question_answer_detail(request, slug):
    """
    Display all :model:`test.Test` per individual :model:`question.Question`.

    :param request: The requested question.
    :param slug: The identification (slug) of the request.
    """

    answers = Answer.objects.filter(question__slug=slug)

    context = {
        "answers": answers,
        "question": answers.first().question,
    }

    return render(
        request,
        "answer/question_answer_detail.html",
        context
    )


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


def answer_form(request):
    """
    Display the form which creates a new :model:`answer.Answer`.

    **Context**

    ``answer_form``
        An instance of :form:`answer.AnswerForm`.

    **Template**

    :template:`answer/answer_form.html`.
    """

    if request.method == 'GET':

        return render(request, 'answer_form.html', {'form': AnswerForm()})

    if request.method == "POST":

        form = AnswerForm(request.POST)

        if form.is_valid():
            form.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "New answer created"
            )

            return HttpResponseRedirect('tests')

    return render(request, "answer/answer_form.html", {'form': AnswerForm()})


def answer_edit(request, id):
    obj = get_object_or_404(Answer, id=id)
    # form = AnswerNew()
    # form = AnswerNew(request.POST, instance=obj)

    # if form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect('test/')

    # context = {
    #     'form': obj
    # }

    # return render(request, 'answer_edit.html', context)

    if request.method == 'GET':

        context = {
            'form': AnswerForm(instance=obj),
            'id': id
        }

        return render(request, 'answer_form.html', context)

    elif request.method == 'POST':

        form = AnswerForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            messages.success(request, "Answer updated")
            return HttpResponseRedirect('tests')

        else:
            messages.error(request, "An error occurred during update")
            return render(request, 'answer_form.html', {'form': form})


def answer_delete(request, id):
    obj = get_object_or_404(Answer, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('test/')

    return render(request, 'answer_delete.html')
