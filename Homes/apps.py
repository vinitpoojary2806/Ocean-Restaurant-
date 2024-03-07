from django.apps import AppConfig


class HomesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Homes'


from django.apps import AppConfig


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking_app'