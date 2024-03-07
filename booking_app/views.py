from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from booking_app.models import  Booking

from django.http import HttpResponse

def make_payment(request):
    if request.method == 'POST':
            user = request.user
            flight_name = request.POST.get('flight_name')
            source = request.POST.get('source')
            destination = request.POST.get('destination')
            departure_date = request.POST.get('departure_date')
            return_date = request.POST.get('return_date') 
            card_number = request.POST.get('card_number') 
            expiration_date = request.POST.get('expiration_date') 
            cvv = request.POST.get('cvv') 
            obj = Booking.objects.create(
                 flight_name = flight_name,
                 user = user,
            source = source,
            destination = destination,
            departure_date = departure_date,
            return_date = return_date ,
            card_number = card_number,
            expiration_date = expiration_date,
            cvv = cvv
            )

            obj.save()
            return redirect('/booking_app/payment_success/')
    return render(request, 'booking_app/book_flight.html')

def payment_success(request):
    return render(request, 'booking_app/payment_success.html')

def display_table(request):
     user = request.user
     obj = Booking.objects.filter(user=user)
     return render(request, 'booking_app/table.html', {'bookings': obj })

def getBill(request, id):
     obj = Booking.objects.filter(id=id)
     return render(request, 'booking_app/ticket.html', {'bookings': obj})