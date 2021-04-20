from django.shortcuts import render,redirect
from .models import Image, Category, Product, Admin, Order, ProductToOrder
from django.contrib import messages
from mainapp.forms import ImgForm
from mainapp.models import Image




def index(request):
    context={
        'products' : Product.objects.all()
    }
    return render(request,'index.html', context)


def cart(request):
    
    return render(request,'cart.html')
    
def dashboard(request):
    return render(request,'dashboard.html')

def products(request):
    context = {
        'products' : Product.objects.all(),
    }
    
    return render(request,'products.html', context)

def product_edit(request, id):
    context = {
        'product' : Product.objects.get(id = id),
        'categories' : Category.objects.all()
    }
    return render(request, 'productedit.html', context)


def upload_img(request):
    pass



def editproduct(request, id):
    
    updated_product = Product.objects.get(id = id)
    updated_product.name = request.POST['name']
    updated_product.desc = request.POST['desc']
    updated_product.category = Category.objects.filter(name=request.POST['categories'])[0]
    updated_product.category = request.POST['category']
    updated_product.save()
    return redirect('dashboard')


def showproduct(request):
    context = {
        'products' : Product.objects.all()
    }
    return render(request,'product_show.html')


def buypage(request, id):
    context={
        'product' : Product.objects.get(id=id),
    }
    return render(request, 'product_info.html', context)



def new_product(request):
    return render(request, 'add.html')

def addproduct(request):
    new_product = Product.objects.create(
        name=request.POST['name'],
        desc=request.POST['desc'],
        price=request.POST['price'],
    )
    return redirect('dashboard')

