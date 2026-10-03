from django.urls import path
from . import views
from .views import AnswerEdit


urlpatterns = [
    path('delete/<int:id>', views.answer_delete, name='answer_delete'),
    path('edit/<int:pk>', AnswerEdit.as_view(), name='answer_edit'),
    path('new/', views.answer_form, name='answer_form'),
]
