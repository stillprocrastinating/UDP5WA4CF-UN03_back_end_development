from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.question_detail, name='question_detail'),
    path('', views.QuestionList.as_view(), name='questions'),
]
