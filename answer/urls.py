from django.urls import path
from . import views
from .views import AnswerEdit, AnswerForm


urlpatterns = [
    path('delete/<int:id>', views.answer_delete, name='answer_delete'),
    path('edit/<int:pk>', AnswerEdit.as_view(), name='answer_edit'),
    path('new/', AnswerForm.as_view(), name='answer_form'),
]
