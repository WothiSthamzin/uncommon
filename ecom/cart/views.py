from django.shortcuts import render, get_object_or_404
from .cart import Cart
from uncommonstore.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    """
    View to display the summary of items in the cart.

    Retrieves the current cart, the products in it, their quantities,
    and the total cost. Renders the cart summary template with the
    gathered data.

    Args:
        request (HttpRequest): The request object for the current session.

    Returns:
        HttpResponse: Rendered cart summary template with cart data.
    """
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {'cart_products': cart_products, "quantities":quantities, "totals":totals})

def cart_add(request):
    """
    View to add a product to the cart.

    Checks for a POST request, retrieves the product ID and quantity
    from the request, adds the product to the cart, and returns
    the updated cart quantity in a JSON response.

    Args:
        request (HttpRequest): The request object for the current session.

    Returns:
        JsonResponse: JSON response containing the updated cart quantity.
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response

def cart_delete(request):
    """
    View to delete a product from the cart.

    Checks for a POST request, retrieves the product ID from the request,
    deletes the product from the cart, and returns a JSON response with
    the deleted product ID.

    Args:
        request (HttpRequest): The request object for the current session.

    Returns:
        JsonResponse: JSON response containing the ID of the deleted product.
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id })
        messages.success(request, ("Item Deleted From Shopping Cart..."))
        return response

def cart_update(request):
    """
    View to update the quantity of a product in the cart.

    Checks for a POST request, retrieves the product ID and new quantity
    from the request, updates the cart, and returns a JSON response with
    the updated quantity.

    Args:
        request (HttpRequest): The request object for the current session.

    Returns:
        JsonResponse: JSON response containing the updated quantity of the product.
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.success(request, ("your Cart Has Been Updated..."))
        return response
