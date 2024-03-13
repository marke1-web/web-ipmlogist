from django.contrib import admin
from .models import DocumentContract, Company, Employee

# Register your models here.

admin.site.register(DocumentContract)
admin.site.register(Company)
admin.site.register(Employee)
