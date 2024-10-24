Cart Documentation
==================

This file documents the cart functionalities in the Uncommon Store application.

.. class:: Cart

    A class representing the shopping cart functionality.

.. method:: __init__(self, request)

    Initializes the cart, associating it with the user's session.

.. method:: add(self, product, quantity)

    Adds a specified product and quantity to the cart.

.. method:: cart_total(self)

    Calculates the total price of items in the cart.

.. method:: __len__(self)

    Returns the number of items in the cart.

.. method:: get_prods(self)

    Retrieves the products currently in the cart.

.. method:: get_quants(self)

    Retrieves the quantities of products in the cart.

.. method:: update(self, product, quantity)

    Updates the quantity of a specified product in the cart.

.. method:: delete(self, product)

    Deletes a specified product from the cart.
