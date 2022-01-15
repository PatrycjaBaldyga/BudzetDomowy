from django.contrib import admin
from .models import IncomeExpense_Info

class IncomeExpense_Admin(admin.ModelAdmin):
    list_display=("title","amount","category","date","type")
    
admin.site.register(IncomeExpense_Info,IncomeExpense_Admin)

