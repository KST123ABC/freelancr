import self as self
from django.db import models
from django.core.validators import *
from dj.choices import Choices, Choice
from phonenumber_field.modelfields import PhoneNumberField
from django import forms

# Create your models here.

class Gender(Choices):
    male = Choice("male")
    female = Choice("female")
    not_specified = Choice("not specified")

class Who(Choices):
    company = Choices("Are you a Company?")
    freelancer = Choices("Are you a Freelancer?")

class Freelancer(models.Model):
    """
    A single freelancer and all the information about the freelancer
    """

    firstName = models.CharField(
        max_length=50,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z0-9]$', message='Only alphanumerics can be input')],
        primary_key = True
    )

    middleInitial = models.CharField(
        max_length=1,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z0-9]$', message='Only alphanumerics can be input')],
        primary_key = False
    )

    lastName = models.CharField(
        max_length=50,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z0-9]$', message='Only alphanumerics can be input')],
        primary_key=True
    )

    gender = Gender.from_id(self.gender)

    phoneNumber = PhoneNumberField(primary_key=True),

    email = models.EmailField(default="",primary_key=True)


class signup(models.Model):

    firstName = models.CharField(
        max_length=50,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z0-9]$', message='Only alphanumerics can be input')],
        primary_key=True
    )

    middleInitial = models.CharField(
        max_length=1,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z0-9]$', message='Only alphanumerics can be input')],
        primary_key=False
    )

    lastName = models.CharField(
        max_length=50,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z0-9]$', message='Only alphanumerics can be input')],
        primary_key=True
    )

    gender = Gender.from_id(self.gender)

    phoneNumber = PhoneNumberField(primary_key=True),

    email = models.EmailField(default="", primary_key=True)

    username = models.CharField(
        min_length=8,
        max_length=50,
        message = 'Minimum length of username should be 8'
    )

    password = models.CharField(
        min_length=8,
        max_length=50,
        message = 'Minimum length of password should be 8'
    )