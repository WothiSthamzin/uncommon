from django.db import models
# To know when customer placed an order
import datetime

# Create your models here.
class Category(models.Model):
    """
    Represents a product category.

    Attributes:
        name (str): The name of the category.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    # To fix spelling error on '/admin' for "Categories" 
    class Meta:
        """
        Meta options for the Category model.
        """
        verbose_name_plural = 'categories'


# Customers
class Customer(models.Model):
    """
    Represents a customer.

    Attributes:
        first_name (str): The customer's first name.
        last_name (str): The customer's last name.
        phone (str): The customer's phone number.
        email (str): The customer's email address.
        password (str): The customer's password.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# All products
class Product(models.Model):
    """
    Represents a product for sale.

    Attributes:
        name (str): The name of the product.
        price (Decimal): The regular price of the product.
        category (Category): The category to which the product belongs.
        description (str): A description of the product.
        image (ImageField): An image of the product.
        is_sale (bool): Indicates if the product is on sale.
        sale_price (Decimal): The sale price of the product, if applicable.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    # For different Product categories
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product')
    # Whenever an 'product' is on "Sale"
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=7)

    def __str__(self):
        return self.name

# Customer Orders
class Order(models.Model):
    """
    Represents a customer's order.

    Attributes:
        product (Product): The product being ordered.
        customer (Customer): The customer placing the order.
        quantity (int): The quantity of the product being ordered.
        address (str): The delivery address for the order.
        phone (str): The contact phone number for the order.
        date (DateField): The date when the order was placed.
        status (bool): Indicates if the order has been fulfilled.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product