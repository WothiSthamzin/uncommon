# Context Processor Template helps Django finds 'cart'
from .cart import Cart

# Creating 'context processor' for 'cart' to work throughout the site
def cart(request):
    # Return default data from 'cart'
    return {'cart':Cart(request)}