from django.contrib import admin
from.models import Category, Customer, Product, Order

# Register your models here.
"""
Admin configuration for the Uncommon Store application.

This module registers the models with the Django admin site to enable
management through the admin interface.
"""
# Registering the Category model with the admin site.
admin.site.register(Category)
# Registering the Customer model with the admin site.
admin.site.register(Customer)
# Registering the Product model with the admin site.
admin.site.register(Product)
# Registering the Order model with the admin site.
admin.site.register(Order)