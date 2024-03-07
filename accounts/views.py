from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def registerUsers(request):

    if request.method == 'POST':
        firstName = request.POST.get('fname')
        LastName = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('passwd')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username not available")
            return redirect('/accounts/register')
            # return redirect(request, '/register')

        user = User.objects.create(
            first_name = firstName,
            last_name = LastName,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.success(request, "Account Created Successfully....")

        return redirect('/accounts/register')

    return render(request, 'register.html')

def loginUsers(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username..")
            return redirect('/accounts/login')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/accounts/login')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')

def logoutUsers(request):
    logout(request)
    return redirect('/accounts/login')