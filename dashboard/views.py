from django.shortcuts import render

# Create your views here.
def index(request):
    # categories = Category.objects.all()
    # expenses = Expense.objects.filter(owner=request.user)
    context = {
        'dashboard': 'dashboard',
        'page_obj': 'page_obj',
        'currency': 'currency'
    }
    return render(request, 'dashboard/index.html', context)