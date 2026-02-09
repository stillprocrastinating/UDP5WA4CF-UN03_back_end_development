from django.urls import path
from . import views


urlpatterns = [
    path('', views.ModuleList.as_view(), name='modules'),
]
