from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model = User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('image',
                  'identity',
                  'firstName',
                  'middleInitial',
                  'lastName',
                  'name',
                  'details',
                  'phoneNumber',
                  'email',
                  'password',
                  'confirmPassword'
                  )

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )
class FreelancerUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = (
        'image1',
        'firstName',
        'middleInitial',
        'lastName',
        'phoneNumber',
        'email',
        'password'
        )

class CompanyUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = (
        'image',
        'name',
        'details',
        'email',
        'password'
        )
