import json
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import IncomeExpense_Info
from django.core.paginator import Paginator

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

    