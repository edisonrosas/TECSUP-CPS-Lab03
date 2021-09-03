from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def product(request):
    return render(request, 'store/product.html')

def about(request):
    return render(request, 'store/about.html')

def shop(request):
    return render(request, 'store/shop.html')