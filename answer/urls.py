from django.urls import path
from .views import AnswerDelete, AnswerEdit, AnswerForm


urlpatterns = [
    path('delete/<int:pk>', AnswerDelete.as_view(), name='answer_delete'),
    path('edit/<int:pk>', AnswerEdit.as_view(), name='answer_edit'),
    path('new/', AnswerForm.as_view(), name='answer_form'),
]
