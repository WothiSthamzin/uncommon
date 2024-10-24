Models Documentation
=====================

This file documents the models defined in the Uncommon Store application.

.. model:: Category

    Represents a product category.

    **Fields:**
    - `name`: A `CharField` representing the category name.

.. model:: Customer

    Represents a customer in the store.

    **Fields:**
    - `first_name`: A `CharField` for the customer's first name.
    - `last_name`: A `CharField` for the customer's last name.
    - `phone`: A `CharField` for the customer's phone number.
    - `email`: A `CharField` for the customer's email address.
    - `password`: A `CharField` for the customer's password.

.. model:: Product

    Represents a product in the store.

    **Fields:**
    - `name`: A `CharField` for the product name.
    - `price`: A `DecimalField` for the product price.
    - `category`: A `ForeignKey` to the `Category` model.
    - `description`: A `CharField` for product description (optional).
    - `image`: An `ImageField` for the product image.
    - `is_sale`: A `BooleanField` indicating if the product is on sale.
    - `sale_price`: A `DecimalField` for the sale price (if applicable).

.. model:: Order

    Represents a customer's order.

    **Fields:**
    - `product`: A `ForeignKey` to the `Product` model.
    - `customer`: A `ForeignKey` to the `Customer` model.
    - `quantity`: An `IntegerField` for the quantity ordered.
    - `address`: A `CharField` for the delivery address (optional).
    - `phone`: A `CharField` for the customer's phone number (optional).
    - `date`: A `DateField` for the order date.
    - `status`: A `BooleanField` indicating the order status.
