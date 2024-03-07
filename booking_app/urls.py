from django.urls import path
from .views import make_payment,payment_success,getBill, display_table

app_name = "booking_app"

urlpatterns = [
    path('make_payment/', make_payment, name='make_payment'),
    path('payment_success/', payment_success, name='payment_success'),
    path('details',display_table, name="showtables" ),
    path('bills/<id>', getBill, name="printBill")
]