from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.TestList.as_view(), name='tests'),
]
