from django.shortcuts import render
from challenge4.models import PortfolioItem, Hobby

def nav_bar():
    return

# Create your views here.
def home(request):
    context = {}
    return render(request, 'challenge4/home.html', context)

def hobbies_detail(request, hobby_id):
    hobby = Hobby.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'challenge4/hobbies_detail.html', context)

def portfolio_detail(request, item_id):
    portfolio_item = PortfolioItem.objects.get(pk=item_id)
    context = {
        'portfolio_item': portfolio_item
    }
    return render(request, 'challenge4/portfolio_detail.html', context)

def hobbies(request):
    context = {
        'hobby_list': Hobby.objects.all()
    }
    return render(request, 'challenge4/hobbies.html', context)

def portfolio(request):
    context = {
        'portfolio_list': PortfolioItem.objects.all()
    }
    return render(request, 'challenge4/portfolio.html', context)

def contact(request):
    context = {}
    return render(request, 'challenge4/contact.html', context)