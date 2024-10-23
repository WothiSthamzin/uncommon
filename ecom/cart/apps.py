from django.apps import AppConfig


class CartConfig(AppConfig):
    """
    Configuration for the Cart application.

    This class configures the Cart app and sets the default
    auto field type for primary keys.

    Attributes:
        default_auto_field (str): The type of auto field to use for primary keys.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
