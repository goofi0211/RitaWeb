from django.shortcuts import render,get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm
# Create your views here.
def product_list(request, ):
    products = Product.objects.filter(available=True)
    is_login=request.session.get('is_login')
    return render(request,
                  'shop/product/list.html',
                  {'products': products,'is_login':is_login})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    is_login=request.session.get('is_login')
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form,'is_login':is_login})