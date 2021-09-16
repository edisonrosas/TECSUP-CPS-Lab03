from django.core import paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import user, product
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Page, Paginator
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def producto(request, product_id):
    p = product.objects.get(id=product_id)
    a = product.objects.filter(categoria=p.categoria)[:4]
    context = {'producto' : p, 'productos' : a}
    return render(request, 'store/product.html',context)

def index(request):
    
    productos = product.objects.all() #se cargarán solo 8 datos hasta que sea viable la paginación
    pagina = request.GET.get('page', 1) 
    

    try:
        paginator = Paginator(productos, 4)
        productos = paginator.page(pagina)

    except:
        raise Http404

    context = {
        'productos':productos,
        'paginator':paginator,
    }


    return render(request, 'store/index.html',context)


def productos(request):
#PRODUCTO SELECCIONADO

    #categoria -> tiene el valor de la categoria del producto seleccionado
    category=''

#RELATED PRODUCTS

    #Se deben filtrar según la categoria del producto seleccionado actualmente
    products_related=product.objects.filter(categoria=category)[:8]
    dictproducts={'products_related':products_related}

    #se envian los products_related junto con los del product seleccionado
    return render(request, 'store/product.html', dictproducts)

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

# FORM LOGIN

def login(request):
    if request.method == 'POST':
        try:
            detalleUser = user.objects.get(Correo=request.POST['correo'], clave=request.POST['password'])
            print("Usuario=", detalleUser)
            request.session['Correo']=detalleUser.Correo
            return redirect('store:index')
        except user.DoesNotExist as e:
            messages.success(request, 'Correo Electrónico o Password no es correcto..!')
    return render(request, 'store/login.html')
