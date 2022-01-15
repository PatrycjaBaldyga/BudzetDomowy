import json
import re
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib import messages
import budget
from .models import IncomeExpense_Info
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.db.models import Sum
from django.http import JsonResponse
from django.utils import timezone
import datetime

# widok strony głównej
def index(request):
    
    #jeżeli metoda get to wyświetl obiekty (+paginacja)
    if request.method == "GET":
        incomeexpense_info = IncomeExpense_Info.objects.order_by('-date')
        paginator = Paginator(incomeexpense_info, 10)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        context = {
           'page_obj' : page_obj
        }
        return render(request, 'budget/index.html', context)
    
    #jeżeli metoda post to zapisz podane pola
    elif request.method == "POST":
        incomeexpense_info = IncomeExpense_Info.objects.order_by('-date')
        title = request.POST["title"]
        type = request.POST["type"]
        amount = request.POST["amount"]
        date = request.POST["date"]
        category = request.POST["category"]
        add = IncomeExpense_Info(title=title,type=type,amount=amount,date=date,category=category)
        add.save()
        paginator = Paginator(incomeexpense_info, 10)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        context = {
            'page_obj' : page_obj
            }
        return render(request, 'budget/index.html', context)
    
    #jezeli metoda delete to usuń obiekt o tym id
    elif request.method == "DELETE":
        id = json.loads(request.body)['id']
        incomeexpense_info = IncomeExpense_Info.objects.get(id=id)
        incomeexpense_info.delete()
        return HttpResponse('')
    
    return HttpResponseRedirect('')


"""
def expense_month(request):
    todays_date = datetime.date.today()
    one_month_ago = todays_date-datetime.timedelta(days=30)
    addmoney = IncomeExpense_Info.objects.filter(Date__gte=one_month_ago,Date__lte=todays_date)
    finalrep ={}
 
    def get_category(incomeexpense_info):
        # if incomeexpense_info.type=="Expense":
        return incomeexpense_info.category    
    Category_list = list(set(map(get_category,addmoney)))
 
    def get_expense_category_amount(Category,add_money):
        amount = 0 
        filtered_by_category = addmoney.filter(Category = Category,add_money="Expense") 
        for item in filtered_by_category:
            amount+=item.amount
        return amount
 
    for x in addmoney:
        for y in Category_list:
            finalrep[y]= get_expense_category_amount(y,"Expense")
 
    return JsonResponse({'expense_category_data': finalrep}, safe=False)
 
 
def stats(request):
    if request.session.has_key('is_logged') :
        todays_date = datetime.date.today()
        one_month_ago = todays_date-datetime.timedelta(days=30)
        incomeexpense_info = IncomeExpense_Info.objects.filter(Date__gte=one_month_ago,Date__lte=todays_date)
        sum = 0 
        for i in incomeexpense_info:
            if i.add_money == 'Expense':
                sum=sum+i.amount
        incomeexpense_info.sum = sum
        sum1 = 0 
        for i in incomeexpense_info:
            if i.add_money == 'Income':
                sum1 =sum1+i.amount
        incomeexpense_info.sum1 = sum1
        x= user1.userprofile.Savings+incomeexpense_info.sum1 - incomeexpense_info.sum
        y= user1.userprofile.Savings+incomeexpense_info.sum1 - incomeexpense_info.sum
        if x<0:
            messages.warning(request,'Your expenses exceeded your savings')
            x = 0
        if x>0:
            y = 0
        incomeexpense_info.x = abs(x)
        incomeexpense_info.y = abs(y)
        return render(request,'home/stats.html',{'addmoney':incomeexpense_info})
 
def expense_week(request):
    todays_date = datetime.date.today()
    one_week_ago = todays_date-datetime.timedelta(days=7)
    addmoney = IncomeExpense_Info.objects.filter(Date__gte=one_week_ago,Date__lte=todays_date)
    finalrep ={}
 
    def get_Category(incomeexpense_info):
        return incomeexpense_info.Category
    Category_list = list(set(map(get_Category,addmoney)))
 
 
    def get_expense_category_amount(Category,add_money):
        amount = 0 
        filtered_by_category = addmoney.filter(Category = Category,add_money="Expense") 
        for item in filtered_by_category:
            amount+=item.amount
        return amount
 
    for x in addmoney:
        for y in Category_list:
            finalrep[y]= get_expense_category_amount(y,"Expense")
 
    return JsonResponse({'expense_category_data': finalrep}, safe=False)
    
def weekly(request):
    if request.session.has_key('is_logged') :
        todays_date = datetime.date.today()
        one_week_ago = todays_date-datetime.timedelta(days=7)
        incomeexpense_info = IncomeExpense_Info.objects.filter(Date__gte=one_week_ago,Date__lte=todays_date)
        sum = 0 
        for i in incomeexpense_info:
            if i.add_money == 'Expense':
                sum=sum+i.amount
        incomeexpense_info.sum = sum
        sum1 = 0 
        for i in incomeexpense_info:
            if i.add_money == 'Income':
                sum1 =sum1+i.amount
        incomeexpense_info.sum1 = sum1
        x= user1.userprofile.Savings+incomeexpense_info.sum1 - incomeexpense_info.sum
        y= user1.userprofile.Savings+incomeexpense_info.sum1 - incomeexpense_info.sum
        if x<0:
            messages.warning(request,'Your expenses exceeded your savings')
            x = 0
        if x>0:
            y = 0
        incomeexpense_info.x = abs(x)
        incomeexpense_info.y = abs(y)
    return render(request,'home/weekly.html',{'incomeexpense_info':incomeexpense_info})

def info_year(request):
    todays_date = datetime.date.today()
    one_week_ago = todays_date-datetime.timedelta(days=30*12)
    addmoney = IncomeExpense_Info.objects.filter(Date__gte=one_week_ago,Date__lte=todays_date)
    finalrep ={}
 
    def get_Category(incomeexpense_info):
        return incomeexpense_info.Category
    Category_list = list(set(map(get_Category,addmoney)))
 
    def get_expense_category_amount(Category,add_money):
        amount = 0 
        filtered_by_category = addmoney.filter(Category = Category,add_money="Expense") 
        for item in filtered_by_category:
            amount+=item.amount
        return amount
 
    for x in addmoney:
        for y in Category_list:
            finalrep[y]= get_expense_category_amount(y,"Expense")
 
    return JsonResponse({'expense_category_data': finalrep}, safe=False)
 
def info(request):
    return render(request,'home/info.html')
"""