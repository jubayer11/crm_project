from django import forms
from django.contrib.auth.models import User, Group
from django_registration.forms import RegistrationForm

from users.models import CustomUser


class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class CustomGroupForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
