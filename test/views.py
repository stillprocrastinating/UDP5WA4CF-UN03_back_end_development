from answer.models import Answer
from answer.views import test_answer_detail
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Test


class TestList(ListView):
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


class TestForm(CreateView):
    model = Test
    fields = ['id', 'date', 'type', 'participant_number',]
    success_url = reverse_lazy('tests')

    def form_valid(self, form):
        form.instance.tester = self.request.user
        messages.success(self.request, "New test created")
        return super(TestForm, self).form_valid(form)


class TestEdit(UpdateView):
    model = Test
    fields = ['id', 'date', 'type', 'participant_number',]
    success_url = reverse_lazy('tests')

    def form_valid(self, form):
        messages.success(self.request, "The test was updated")
        return super(TestEdit, self).form_valid(form)


class TestDelete(DeleteView):
    model = Test
    context_object_name = 'test'
    success_url = reverse_lazy('tests')

    def form_valid(self, form):
        messages.success(self.request, "The test was deleted")
        return super(TestDelete, self).form_valid(form)
