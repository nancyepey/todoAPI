from django.shortcuts import render

from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Category, Expense
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
# from userpreferences.models import UserPreference
import datetime



def index(request):
    # categories = Category.objects.all()
    # expenses = Expense.objects.filter(owner=request.user)
    # paginator = Paginator(expenses, 5)
    # page_number = request.GET.get('page')
    # page_obj = Paginator.get_page(paginator, page_number)
    # currency = UserPreference.objects.get(user=request.user).currency
    context = {
        'expenses': 'expenses',
        'page_obj': 'page_obj',
        'currency': 'currency'
    }
    return render(request, 'todo/index.html', context)

