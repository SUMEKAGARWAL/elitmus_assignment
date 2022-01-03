from django.shortcuts import render, HttpResponse, redirect
from django.utils import html
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image



# Create your views here.
def index(request):
    return render(request, 'index.html') 


def registration(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            user_form.save()
            print("I shd go to ground now.")
            return HttpResponse("<h1>Registration successful. Now you can go back and login.<h1>")
    else:
        user_form = RegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form} )

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(request, username = cd["username"], password = cd["password"])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home.html')
                else:
                    return HttpResponse("<h1>Login Disable</h1>")
            else:
                return HttpResponse("<h1> Invalid Login</h1>")
    else:
        form = LoginForm()

    return render( request, "login.html", {"form":form})

@login_required
def user_logout(request):
    logout(request)
    print("I am into logout")
    return HttpResponse("<h1>Logout successfully</h1>")


def create(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            img=Image.objects.all()
            return render(request,"home.html",{"img":img,"obj":obj}) #showing the adv at home page
    else:
        form=ImageForm()
        img=Image.objects.all()
        return render(request,"create.html",{"img":img,"form":form})
    

def home(request):
    img=Image.objects.all()
    return render(request, "home.html", {"img":img})


def delete_contact(request, pk):
    curr_contact = Image.objects.get(id=pk)
    curr_contact.delete()
    # messages.error(request, "deleted successfully!!")  # this was getting printed on the admin site with a red mark which was daunting
    return redirect('/home')