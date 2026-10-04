from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
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


# def answer_form(request):
#     """
#     Display the form which creates a new :model:`answer.Answer`.

#     **Context**

#     ``answer_form``
#         An instance of :form:`answer.AnswerForm`.

#     **Template**

#     :template:`answer/answer_form.html`.
#     """

#     if request.method == 'GET':

#         return render(request, 'answer_form.html', {'form': AnswerForm()})

#     if request.method == "POST":

#         form = AnswerForm(request.POST)

#         if form.is_valid():
#             form.save()

#             messages.add_message(
#                 request,
#                 messages.SUCCESS,
#                 "New answer created"
#             )

#             return HttpResponseRedirect('tests')

#     return render(request, "answer/answer_form.html", {'form': AnswerForm()})


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


def answer_delete(request, id):
    obj = get_object_or_404(Answer, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('test/')

    return render(request, 'answer_delete.html')
