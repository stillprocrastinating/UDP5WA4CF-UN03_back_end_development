from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.test_new, name='test_new'),
    path('<slug:slug>/', views.test_detail, name='test_detail'),
    path('', views.TestList.as_view(), name='tests'),
]
