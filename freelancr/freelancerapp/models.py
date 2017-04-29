import self
from django.db import models
from django.core.validators import *
from dj.choices import Choices, Choice
from django.db.models import ImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.models import User

import os
# Create your models here.
<<<<<<< HEAD


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Gender(Choices):
    male = Choice("male")
    female = Choice("female")
    not_specified = Choice("not specified")

class ProfileInfo(models.Model):
	user = models.OneToOneField(User, related_name='profileinfo', on_delete = models.CASCADE)
    image1 = ImageField(upload_to="media", blank=True, null=True)
    image2 = ImageField(upload_to="media", blank=True, null=True)
    image3 = ImageField(upload_to="media", blank=True, null=True)
    #False -- talent, True -- hire
    identity = BooleanField(default = False)
    # Freelancer field
    firstName = models.CharField(
        max_length=50,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z]$', message='Only letters can be input')],
        primary_key = True
    )
    middleInitial = models.CharField(
        max_length=1,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z]$', message='Only letters can be input')],
        null = True,
    )
    lastName = models.CharField(
        max_length=50,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z]$', message='Only letters can be input')],
        primary_key=True
    )
    gender = Gender.from_id(self.gender)
    # Company field
    name = models.CharField(
        max_length=50,
        default="",
        primary_key=True
    )
    details = models.CharField(
        max_length=500,
        default="",
        null = True
    )
    # Common field
    phoneNumber = PhoneNumberField(primary_key=True)
    email = models.EmailField(default="",primary_key=True)

class Skill(models.Model):
    skillName = Textfield(primary_key = True)

'''
=======
>>>>>>> 1b375eed7744b0d194490ec907880d0433c9faaf
class Gender(Choices):
    male = Choice("male")
    female = Choice("female")
    not_specified = Choice("not specified")

class UserChoice(Choices):
    company = Choices("Are you a Company?")
    freelancer = Choices("Are you a Freelancer?")

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class User(models.Model):
    identity = UserChoice(),
    image1 = ImageField(upload_to=get_image_path, blank=True, null=True),
    image2 = ImageField(upload_to=get_image_path, blank=True, null=True),
    image3 = ImageField(upload_to=get_image_path, blank=True, null=True)

class Freelancer(models.Model):
    """
    A single freelancer and all the information about the freelancer
    """

    firstName = models.CharField(
        max_length=50,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z]$', message='Only letters can be input')],
        primary_key = True
    )

    middleInitial = models.CharField(
        max_length=1,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z]$', message='Only letters can be input')],
        null = True,
    )

    lastName = models.CharField(
        max_length=50,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z]$', message='Only letters can be input')],
        primary_key=True
    )

    gender = Gender.from_id(self.gender)

    phoneNumber = PhoneNumberField(primary_key=True),

    email = models.EmailField(default="",primary_key=True)



class Company(models.Model):
    name = models.CharField(
        max_length=50,
        default="",
        primary_key=True
    )
    details = models.CharField(
        max_length=500,
        default="",
        null = True
    )

'''
