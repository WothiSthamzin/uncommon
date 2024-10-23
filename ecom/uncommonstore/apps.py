from django.apps import AppConfig


class UncommonstoreConfig(AppConfig):
    """
    Configuration for the Uncommon Store application.

    This class configures the Uncommon Store app and sets the default
    auto field type for primary keys.

    Attributes:
        default_auto_field (str): The type of auto field to use for primary keys.
        name (str): The name of the application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uncommonstore'
