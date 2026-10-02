from django.urls import path
from . import views


urlpatterns = [
    path('delete/<slug:slug>', views.answer_delete, name='answer_delete'),
    path('edit/<slug:slug>', views.answer_edit, name='answer_edit'),
    path('new/', views.answer_new, name='answer_new'),
]
