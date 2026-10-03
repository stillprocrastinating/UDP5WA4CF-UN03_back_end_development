from django.urls import path
from . import views


urlpatterns = [
    path('delete/<int:id>', views.answer_delete, name='answer_delete'),
    path('edit/<int:id>', views.answer_edit, name='answer_edit'),
    path('new/', views.answer_form, name='answer_form'),
]
