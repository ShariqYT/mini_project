from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def index(request):
    return render(request, 'authentication/index.html')


def register(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username, pass1, mobile)
        myuser.username = username
        myuser.mobile = mobile
        myuser.save()

        messages.success(request, "Your Account has been created.")

        return redirect('login')

    return render(request, 'authentication/register.html')


def signin(request):

    if request.method == "POST":    
        username = request.POST['username']
        mobile = request.POST['mobile']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1, mobile=mobile)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "authentication/index.html", {'username':username})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('index')

    return render(request, 'authentication/login.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('index')