from django.db import models
from django.utils.timezone import now

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