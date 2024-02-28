from django.contrib import admin
from .models import JournalContractType, JournalContract
# Register your models here.
admin.site.register(JournalContractType)
admin.site.register(JournalContract)