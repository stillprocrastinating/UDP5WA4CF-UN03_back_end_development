from django.urls import path
from . import views


urlpatterns = [
    path('new/answers/', views.answer_new, name='answer_new_answers'),
    path('new/question/', views.answer_new, name='answer_new_question'),
    path('new/test/', views.answer_new, name='answer_new_test'),
]
