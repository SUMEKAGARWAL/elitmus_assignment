from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image

#from myproject.myapp.models import Image

class RegistrationForm(UserCreationForm): #reg form is inherited from user creation form 
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("caption", "image")

