from django.http import Http404
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User


# Create your views here.
def blog(request):
		return render(request, 'core/blog.html')

def category(request):
    productosAll = Producto.objects.all() # SELECT * FROM producto
    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1
    
    try:
        paginator = Paginator(productosAll, 9)
        productosAll = paginator.page(page)
    except:
        raise Http404

    for producto in productosAll:
        precio_descuento = producto.precio - (producto.precio * 0.05) 
        producto.precio_descuento = round(precio_descuento)
    data = {
        'listado': productosAll,
        'paginator': paginator
    }
    return render(request, 'core/category.html', data)

def checkout(request):
    
    carro_compras = CarroCompras.objects.get(usuario=request.user)
    items = carro_compras.items.all()
    total = carro_compras.total()
    
    total_productos = 0
    for item in items:
        total_productos += item.producto.precio * item.cantidad

    valor_fijo = 7560

    total_final = total_productos + valor_fijo

    data = {
        'items': items,
        'total': total,
        'total_final' : total_final
    }

    if request.method == 'POST':
        compra = Compra.objects.create(usuario=request.user)
        for item in items:
            CompraItem.objects.create(compra=compra, carro_item=item)

        carro_compras.compra = compra
        carro_compras.save()
        
        return render(request, 'core/confirmation.html', data)

    return render(request,'core/checkout.html',data)

def confirmation(request):

    carro_compras = CarroCompras.objects.get(usuario=request.user)
    items = carro_compras.items.all()
    total = carro_compras.total()
    


    total_productos = 0
    for item in items:
        total_productos += item.producto.precio * item.cantidad

    valor_fijo = 7560

    total_final = total_productos + valor_fijo

    data = {
        'items': items,
        'total': total,
        'total_final' : total_final
    }

    return render(request,'core/confirmation.html',data)

def miscompras(request):
    return render(request,'core/miscompras.html')

def contact(request):
		return render(request, 'core/contact.html')


def index(request):
    productosAll = Producto.objects.all() # SELECT * FROM PRODUCTO
    for producto in productosAll:
        precio_descuento = producto.precio - (producto.precio * 0.05) 
        producto.precio_descuento = round(precio_descuento)

    data = {
        'listado': productosAll,
    }

    return render(request, 'core/index.html', data)







def singleblog(request):
		return render(request, 'core/single-blog.html')

def singleproduct(request, id):
    producto = Producto.objects.get(id=id) #buscamos un producto por su id (primer campo base de datos y el otro es nuestro)
    data = {
        #'form' : ProductoForm(instance=producto) #Carga la info en el formulario
        'producto' : producto
    }
        

    return render(request,'core/single-product.html',data)


def trackingorder(request):
		return render(request, 'core/tracking-order.html')

def perfil(request):
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name
    return render(request, 'core/perfil.html', {'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name})


def wishlist(request):
        return render(request, 'core/wishlist.html')


## Crud
def add(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) #Recibe toda la info del formulario
        if formulario.is_valid():
            formulario.save() # Commit, Insert into
            #data['msj'] = "Producto guardado correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request,'core/add-product.html', data)

def update(request, id):
    producto = Producto.objects.get(id=id) #buscamos un producto por su id (primer campo base de datos y el otro es nuestro)
    data = {
        'form' : ProductoForm(instance=producto) #Carga la info en el formulario
    }

    if request.method == 'POST':
        #recibe toda la nueva info del formulario
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() #Commit, update 
            #data['msj'] = "Producto modificado correctamente"
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario #actualizar visualmente el formulario 
        

    return render(request,'core/update-product.html',data)

def delete(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="index")


    
def cartadd(request,id):
    producto = Producto.objects.get(id=id)
    carro_compras, created = CarroCompras.objects.get_or_create(usuario=request.user)
    carro_item, item_created = CarroItem.objects.get_or_create(producto=producto, usuario=request.user)
    if not item_created:
        carro_item.cantidad +=1
        carro_item.save()

    carro_compras.items.add(carro_item)
    carro_compras.save()

    return redirect(to='cart')

def cartdel(request,id):
    producto = Producto.objects.get(id=id)
    carro_compras = CarroCompras.objects.get(usuario = request.user)
    carro_item = carro_compras.items.get(producto=producto)
    if carro_item.cantidad > 1:
        carro_item.cantidad -= 1
        carro_item.save()
    else:
        carro_compras.items.remove(carro_item)
        carro_item.delete()
 
    return redirect(to='cart')

def cart(request):
    
    carro_compras = CarroCompras.objects.get(usuario=request.user)
    items = carro_compras.items.all()
    total = carro_compras.total()

    data = {
        'items': items,
        'total': total,
    }

    return render(request,'core/cart.html',data)


def cartdelete(request,id):
    producto = Producto.objects.get(id=id)
    carro_compras = CarroCompras.objects.get(usuario = request.user)
    carro_item = carro_compras.items.get(producto=producto)

    carro_compras.items.remove(carro_item)
    carro_item.delete()
    return redirect(to='cart')

def add_compra(request): 
    carro_compras = CarroCompras.objects.get(usuario = request.user)
    items = carro_compras.items.all()

    compra = Compra.objects.create(usuario = request.user)
    for item in items:
        CompraItem.objects.create(compra = compra, carro_item = item)

    carro_compras.items.clear()
    return redirect(to='confirmation')

def datoscart(request):
    carro_compras = CarroCompras.objects.get(usuario=request.user)
    items = carro_compras.items.all()
    total = carro_compras.total()

    data = {
        'carro_compras': carro_compras,
        'items': items,
        'total': total,
    }

    return render(request, 'core/confirmation.html', data)

def miscompras(request):
    compras = Compra.objects.filter(usuario=request.user)
    data = []

    for compra in compras:
        compra_items = CompraItem.objects.filter(compra=compra)
        total = 0

        for item in compra_items:
            total += item.carro_item.producto.precio * item.carro_item.cantidad

        data.append({'compra': compra, 'total': total})

    return render(request, 'core/miscompras.html', {'data': data})

def detalle(request,id):
    compra = Compra.objects.get(id=id)
    compra_items = CompraItem.objects.filter(compra=compra)
    
    productos = []
    total_compra = 0

    for x in compra_items:
        producto = x.carro_item.producto
        cantidad = x.carro_item.cantidad
        total_producto = producto.precio * cantidad

        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'total': total_producto
        })

        total_compra += total_producto

    data = {
        'compra': compra,
        'productos': productos,
        'total_compra': total_compra
    }

    return render(request, 'core/detalle.html', data)