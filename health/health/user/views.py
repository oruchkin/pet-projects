from django.shortcuts import render
from .forms import SignupForm

# Create your views here.



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
