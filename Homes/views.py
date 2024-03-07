from django.shortcuts import render, redirect
from Homes.models import *
from django.contrib.auth.decorators import login_required



# Create your views here.

def about(request):
    return render(request, 'about.html')

def Homepage(request):
    return render(request, 'index.html')

@login_required(login_url='/account/login')
def bookings(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        numberofpeople = request.POST.get("people")
        description = request.POST.get("msg")
        obj = BookTable.objects.create(
            user = user,
            name = name,
            email = email,
            date = date,
            numberofpeople = numberofpeople,
            description = description
        )
        obj.save() 
        return redirect("/")

    return render(request, 'booking.html')

def contacts(request):
    return render(request, 'contact.html')

def menus(request):
    return render(request, 'menu.html')

def category(request):
    Obj = Category.objects.all()
    return render(request, 'category.html', {'dishes':Obj})

def service(request):
    return render(request, 'service.html')

def teams(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonial.html')

def startersmenus(request):
    return render(request, 'startersmenu.html')

def maincoursemenus(request):
    return render(request, 'maincoursemenu.html')

def chinesemenus(request):
    return render(request, 'chinesemenu.html')

def sizzlersmenus(request):
    return render(request, 'sizzlersmenu.html')

def mocktailsmenus(request):
    return render(request, 'mocktailsmenu.html')

def desertsmenus(request):
    return render(request, 'desertsmenu.html')

def chatbots(request):
    return render(request, 'chatbot.html')

def icecreamfloats(request):
    return render(request, 'icecreamfloat.html')

def drumsofheavens(request):
    return render(request, 'drumsofheaven.html')

def frenchpotatos(request):
    return render(request, 'frenchpotato.html')

def manchuriandrys(request):
    return render(request, 'manchuriandry.html')

def contact(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        obj = ContactTable.objects.create(email=email, description=desc)
        obj.save()
        return render(request, 'about.html')
    
    return render(request, 'contact.html')

def viewDishes(request, id):
    obj = Dishes.objects.filter(id=id)
    return render(request,'frenchpotato.html', {'dishes': obj})

def displayDishes(request, id):
    obj = Dishes.objects.filter(category=id)
    return render(request, 'dishes.html',{"dishes":obj})


def printReport(request, id):
    obj = Dishes.objects.filter(id=id)
    return render(request, 'print.html',{"prints":obj})

