from uncommonstore.models import Product

class Cart():
    # Request : Anytime a user views the 'Cart' page
    def __init__(self, request):
        self.session = request.session
        # If it exists, get current session key 
        cart = self.session.get('session_key')

        # If user is new, create a session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Making sure 'cart' is available throught the site
        self.cart = cart

    # Add to cart function
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def cart_total(self):
        # Getting product IDs
        product_ids = self.cart.keys()
        # Calling up keys in products database
        products = Product.objects.filter(id__in=product_ids)
        # get quantities
        quantities = self.cart
        # Start count from zero
        total = 0
        for key, value in quantities.items():
            # Converting key string into integer for calculations
            key = int(key)
            for product in products:
                if product.id == key:
                    # For products on sale
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.sale_price * value)

        return total

    # Getting length, to count items in cart
    def __len__(self):
        return len(self.cart)
    
    # Getting products
    def get_prods(self):
        # Product IDs stored in a dictionary. Calling relevant products in dictionary 
        product_ids = self.cart.keys()
        # Use IDs to look up products in database model
        products = Product.objects.filter(id__in=product_ids)
        # Return those looked up products
        return products
    
    # Getting quantities ordered
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        # Get Cart
        usercart = self.cart
        # Update Dictionary/cart
        usercart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        # Delete from Dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True


