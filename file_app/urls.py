"""Все ссылки, связанные с частью продажников"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('documents/', views.JournalOrdersView.as_view(), name='documents'),
    path('document-table/', views.DocumentContractTableView.as_view(), name='document_table')
]
