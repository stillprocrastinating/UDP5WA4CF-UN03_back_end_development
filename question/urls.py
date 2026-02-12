from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuestionList.as_view(), name='questions'),
    path('<slug:slug>/', views.question_detail, name='question_detail'),
]
