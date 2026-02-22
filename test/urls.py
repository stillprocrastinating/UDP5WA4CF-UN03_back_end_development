from django.urls import path
from . import views


urlpatterns = [
    #path('<slug:slug>/', views.test_detail, name='test_detail'),
    path('new/', views.test_new, name='test_new'),     # forms.py & test_new.html
    path('', views.TestList.as_view(), name='tests'),
]
