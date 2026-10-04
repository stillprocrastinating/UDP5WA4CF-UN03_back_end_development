from django.urls import path
from .views import TestDelete, TestEdit, TestForm, TestList, test_detail_page


urlpatterns = [
    path('delete/<slug:slug>', TestDelete.as_view(), name='test_delete'),
    path('edit/<slug:slug>', TestEdit.as_view(), name='test_edit'),
    path('new/', TestForm.as_view(), name='test_form'),
    path('id-<slug:slug>/', test_detail_page, name='test_detail'),
    path('', TestList.as_view(), name='tests'),
]
