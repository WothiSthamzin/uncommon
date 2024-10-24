Views Documentation
===================

This file documents the views defined in the `views.py` file of the Uncommon Store application.

.. function:: search(request)

    Handles the search functionality and renders the search results page.

.. function:: category_summary(request)

    Retrieves all categories and renders the category summary page.

.. function:: category(request, foo)

    Displays products of a specific category identified by the `foo` parameter.

.. function:: product(request, pk)

    Renders the details of a specific product identified by its primary key.

.. function:: home(request)

    Renders the homepage displaying all available products.

.. function:: about(request)

    Renders the About page.

.. function:: login_user(request)

    Handles user login. Authenticates the user based on provided credentials.

.. function:: logout_user(request)

    Logs out the user and redirects to the homepage.

.. function:: register_user(request)

    Handles user registration and redirects to the login page upon successful registration.
