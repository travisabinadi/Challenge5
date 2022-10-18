from django.shortcuts import render, redirect
from challenge4.models import PortfolioItem, Hobby
from .forms import PortfolioItemForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    return render(request, 'challenge4/contact.html', {})

def add_portfolio_item(request):
    form = PortfolioItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio'))
    return render(request, 'challenge4/portfolio_item_form.html', context={'form': form})

def update_portfolio_item(request, item_id):
    item = PortfolioItem.objects.get(item_id=item_id)
    form = PortfolioItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect(reverse('portfolio'))

    return render(request, 'challenge4/portfolio_item_form.html', context={'form': form, 'item': item})

def delete_portfolio_item(request, item_id):
    item = PortfolioItem.objects.get(item_id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect(reverse('portfolio'))

    return render(request, 'challenge4/portfolio_item_delete.html', context={'item': item})