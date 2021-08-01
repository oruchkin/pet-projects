from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('index')


def loginView(request):
    if request.method == "POST":
        form = LoginForm()
        uname = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=uname, password=password)
        print("udata is ", user)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "username or password incorect")
    else:
        form = LoginForm()

    return render(request, "users/login.html",{
        "form_key":form
    })

def signup_view(request):
    if request.method == 'POST':
        signform1 = SignupForm(request.POST)
        if signform1.is_valid():
            signform1.save()
            return render(request, "baseapp/index.html")

    else:
        signform = SignupForm()
             
        return render(request, "users/registration.html", {
            "signform_key": signform,
        })

    # else:
    #     render(request, "users/registration.html")

    # return render(request, "users/registration.html", )
