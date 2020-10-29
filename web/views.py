from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from web.models import User,Token,Expense,Income

@csrf_exempt
def submit_expense(request):
    """user submit an expense"""

    print("it works")
    print(request.POST)
    #TODO: validate data is one of them might be in valid of missed
    this_text = request.POST['text']
    this_token = request.POST['token']
    this_amount = request.POST['amount']
    if 'date' in request.POST:
        this_date = request.POST['date']
    else:
       this_date = datetime.now()
    #learn token--token
    this_user = User.objects.filter(token__token = this_token).get()
    Expense.objects.create(user=this_user, amount=this_amount,text = this_text, date = this_date)
    

    print("it works")
    print(request.POST)
    return JsonResponse({
        'status': 'ok',
        }, encoder = JSONEncoder)



@csrf_exempt
def submit_income(request):
    """user submit an income"""

    print("it works")
    print(request.POST)
    #TODO: validate data is one of them might be in valid of missed
    this_text = request.POST['text']
    this_token = request.POST['token']
    this_amount = request.POST['amount']
    if 'date' in request.POST:
        this_date = request.POST['date']
    else:
       this_date = datetime.now()
    #learn token--token
    this_user = User.objects.filter(token__token = this_token).get()
    Income.objects.create(user=this_user, amount=this_amount,text = this_text, date = this_date)
    

    print("it works")
    print(request.POST)
    return JsonResponse({
        'status': 'ok',
        }, encoder = JSONEncoder)






















