"""Все ссылки, связанные с частью продажников"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('documents/', views.DocumentsMainView.as_view(), name='documents'),
    path('companies/', views.CompaniesView.as_view(), name='companies'),
    path('companies/company/<int:pk>', views.CompanyDetailView.as_view(), name='detail_company'),
    path('documents/create-company/<company_type>/', views.CreateCompany.as_view(), name='create_company'),
    path('documents/company/<int:company_id>/create-employee/', views.CreateEmployee.as_view(), name='create_employee'),
    path('document-table/', views.DocumentContractTableView.as_view(), name='document_table'),
    path('document-create/', views.DocumentCreate.as_view(), name='document-create'),
    path('document-update/<int:pk>', views.DocumentUpdate.as_view(), name='document-update'),
    path("document-create/load_companies/", views.load_companies, name="load_companies"),
    path("document-create/load_employees/", views.load_employees, name="load_employees")
]
