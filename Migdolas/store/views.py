from django.shortcuts import render
from django.db.models import Q
from store.models import Product

def home(request):
    return render(request, 'store/main.html')

def store(request):
    context = { }
    return render(request, 'store/store.html', context)

def cart(request):
    context = { }
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = { }
    return render(request, 'store/checkout.html', context)

def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.all()
    
    if query:
        results = results.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
    
    return render(request, 'store/search_results.html', {
        'results': results,
        'query': query
    })
