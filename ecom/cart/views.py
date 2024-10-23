from django.shortcuts import render, get_object_or_404
from .cart import Cart
from uncommonstore.models import Product
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.



def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    # Getting the ordered quantities
    quantities = cart.get_quants
    # Total sum of the order of items
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {'cart_products': cart_products, "quantities":quantities, "totals":totals})

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # Testing for POST
    if request.POST.get('action') == 'post':
        # Get info
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # Call up product database
        product = get_object_or_404(Product, id=product_id)
        # Save to a session
        cart.add(product=product, quantity=product_qty)

        # Getting cart item quantity
        cart_quantity = cart.__len__()

        # return a Json response
        # response = JsonResponse({'Product Name: ':product.name})

        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get info
        product_id = int(request.POST.get('product_id'))
        # Call up delete function in Cart
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id })
        messages.success(request, ("Item Deleted From Shopping Cart..."))
        # return redirect('cart_summary)
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get info
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        # Retrieve the cart from the session
        cart.update(product=product_id, quantity=product_qty)
        # cart_items = request.session.get('cart', {})
        response = JsonResponse({'qty':product_qty})
        messages.success(request, ("your Cart Has Been Updated..."))
        return response

        # # Cart Update
        # if product_qty > 0:
        #     cart_items[product_id] = product_qty
        # else:
        #     # Remove item if quantity is zero
        #     if product_id in cart_items:
        #         del cart_items[product_id]

        # request.session['cart'] = cart_items

        # # To calculate total cost
        # total = 0
        # for product_id, product_qty in cart_items.items():
        #     try:
        #         product = Product.objects.get(id=product_id)
        #         if product.is_sale:
        #             total += product.price * product_qty
        #         else:
        #             total += product.price * product_qty
        #     except Product.DoesNotExist:
        #         continue

        # # cart.update(product=product_id, quantity=product_qty)

        # # Calculate the updated cart total
        # cart_total = cart.cart_total()

        # response = JsonResponse({
        #      'cart_total': cart_total
        # })
        # return response