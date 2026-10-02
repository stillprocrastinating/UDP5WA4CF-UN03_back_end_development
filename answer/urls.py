from django.urls import path
from . import views


urlpatterns = [
    path('delete/<id>', views.answer_delete, name='answer_delete'),
    path('edit/<id>', views.answer_edit, name='answer_edit'),
    path('new/', views.answer_new, name='answer_new'),
]
