# Context Processor Template helps Django finds 'cart'
from .cart import Cart

def cart(request):
    """
    Context processors for providing cart data to templates.

    This function retrieves the cart instance for the current request
    and makes it available in the context for all templates.

    Args:
        request (HttpRequest): The request object for the current session.

    Returns:
        dict: A dictionary containing the cart instance.
    """
    return {'cart':Cart(request)}