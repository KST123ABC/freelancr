from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model = ProfileInfo
        fields = ('image',
                  'identity',
                  'firstName',
                  'middleInitial',
                  'lastName',
                  'name',
                  'details',
                  'phoneNumber',
                  )

class RegistrationForm(UserCreationForm):
    class Meta:
        model = ProfileInfo
        fields = ('image',
                  'identity',
                  'firstName',
                  'middleInitial',
                  'lastName',
                  'name',
                  'details',
                  'phoneNumber',
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
        model = ProfileInfo
        fields = (
        'image',
        'firstName',
        'middleInitial',
        'lastName',
        'phoneNumber',
        )

class CompanyUpdateForm(ModelForm):
    class Meta:
        model = ProfileInfo
        fields = (
        'image',
        'name',
        'details',
        )
