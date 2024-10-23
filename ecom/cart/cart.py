from uncommonstore.models import Product

class Cart():
    """
    A shopping cart class to manage the user's cart session.

    This class is responsible for storing cart items, calculating totals,
    and managing the cart's state within the user's session.

    Attributes:
        session (Session): The session object associated with the user's request.
        cart (dict): A dictionary storing product IDs and their quantities in the cart.
    """
    def __init__(self, request):
        """
        Initializes the Cart instance.

        Args:
            request (HttpRequest): The request object containing session data.
        """
        self.session = request.session
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product, quantity):
        """
        Adds a product to the cart.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product to add.
        """
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def cart_total(self):
        """
        Calculates the total price of items in the cart.

        Returns:
            float: The total price of all products in the cart.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.sale_price * value)

        return total

    def __len__(self):
        """
        Returns the number of items in the cart.

        Returns:
            int: The total number of items in the cart.
        """
        return len(self.cart)
    

    def get_prods(self):
        """
        Retrieves the products currently in the cart.

        Returns:
             A queryset of Product objects in the cart.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        """
        Retrieves the quantities of products in the cart.

        Returns:
            dict: A dictionary of product IDs and their corresponding quantities.
        """
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        """
        Updates the quantity of a specified product in the cart.

        Args:
            product (str): The product ID to update.
            quantity (int): The new quantity for the product.

        Returns:
            dict: The updated cart.
        """
        product_id = str(product)
        product_qty = int(quantity)
        usercart = self.cart
        usercart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self, product):
        """
        Removes a specified product from the cart.

        Args:
            product (str): The product ID to remove.
        """
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True


