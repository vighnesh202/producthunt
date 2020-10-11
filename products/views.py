from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products': products})

@login_required
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            if request.POST['url'].startswith('https://') or request.POST['url'].startswith('http://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.pub_date = timezone.datetime.now()
            #product.votes_total = 1
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {"error": "enter all the fileds"})
    return render(request, 'products/create.html')

def detail(request, product_id):
    detailproduct = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': detailproduct})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        ## either the commented one or the original uncommented return
    
        #detailproduct = get_object_or_404(Product, pk=product_id)
        #return render(request, 'products/detail.html', {'product': detailproduct})

        return redirect('/products/' + str(product.id))  
    

