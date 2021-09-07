from django.shortcuts import redirect, render
from store.models import user
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def product(request):
    return render(request, 'store/product.html')

def about(request):
    return render(request, 'store/about.html')

def shop(request):
    return render(request, 'store/shop.html')



# FORM REGISTER 

def register(request):
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('Correo') and request.POST.get('clave'):
            saverecord = user()
            saverecord.nombre = request.POST.get('nombre')
            saverecord.Correo = request.POST.get('Correo')
            saverecord.clave = request.POST.get('clave')
            saverecord.save()
            messages.success(request, "Usuario Registrado")
            return redirect('store:index')
            

    return render(request, 'store/register.html')