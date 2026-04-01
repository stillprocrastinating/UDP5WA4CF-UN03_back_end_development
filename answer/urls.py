from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.answer_new, name='answer_new'),
    path('<slug:slug>/', views.answer_detail_test, name='answer_detail_test'),
]
