from django.shortcuts import render

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
    results = []
    if query:
        results = Product.objects.filter(
            models.Q(name__icontains=query) | 
            models.Q(description__icontains=query)
        )
    return render(request, 'shop/search_results.html', {
        'results': results,
        'query': query
    })
