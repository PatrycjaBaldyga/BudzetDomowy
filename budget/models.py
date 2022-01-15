from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

SELECT_CATEGORY_CHOICES = [
    ("Jedzenie","Jedzenie"),
    ("Podróże","Podróże"),
    ("Zakupy","Zakupy"),
    ("Rachunki","Rachunki"),
    ("Rozrywka","Rozrywka"),
    ("Wpływ","Wpływ"),
    ("Inne","Inne")
 ]

ADD_EXPENSE_CHOICES = [
     ("Wydatek","Wydatek"),
     ("Wpływ","Wpływ")
 ]

class IncomeExpense_Info(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length = 10 , choices = ADD_EXPENSE_CHOICES )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default = now)
    category = models.CharField( max_length = 50, choices = SELECT_CATEGORY_CHOICES , default ='Jedzenie')
    class Meta:
        db_table:'incomeexpense'

class Stats(models.Model):
        
    def monthly_expenses():
        expense_list = IncomeExpense_Info.objects.filter(type="Wydatek")
        monthly_expense_amount = 0
        for expense in expense_list:
            monthly_expense_amount += expense.amount
    
    def monthly_income(self):
        income_list = IncomeExpense_Info.objects.filter(type="Wpływ")
        monthly_income_amount = 0
        for income in income_list:
            monthly_income_amount += income.amount
       