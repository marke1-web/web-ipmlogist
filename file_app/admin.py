from django.contrib import admin
from .models import DocumentContract, CustomerCompany, Customer, ContractorCompany, Contractor

# Register your models here.

admin.site.register(DocumentContract)
admin.site.register(Customer)
admin.site.register(CustomerCompany)
admin.site.register(ContractorCompany)
admin.site.register(Contractor)
