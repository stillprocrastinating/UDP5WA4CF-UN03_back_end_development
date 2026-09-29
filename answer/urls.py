from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.answer_new, name='answer_new'),
    path('edit/<int:answer_id>', views.answer_edit, name='answer_edit'),
]
