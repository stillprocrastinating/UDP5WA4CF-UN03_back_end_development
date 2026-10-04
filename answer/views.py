from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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


class AnswerForm(CreateView):
    model = Answer
    fields = [
        'test',
        'question',
        'answer1', 'answer2', 'answer3', 'answer4', 'answer5',
    ]
    success_url = reverse_lazy('tests')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "New answer created")
        return super(AnswerForm, self).form_valid(form)


class AnswerEdit(UpdateView):
    model = Answer
    fields = [
        'test',
        'question',
        'answer1', 'answer2', 'answer3', 'answer4', 'answer5',
    ]
    success_url = reverse_lazy('tests')

    def form_valid(self, form):
        messages.success(self.request, "The answer was updated")
        return super(AnswerEdit, self).form_valid(form)


class AnswerDelete(DeleteView):
    model = Answer
    context_object_name = 'answer'
    success_url = reverse_lazy('tests')

    def form_valid(self, form):
        messages.success(self.request, "The answer was deleted")
        return super(AnswerDelete, self).form_valid(form)
