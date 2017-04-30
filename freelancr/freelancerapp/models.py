
from django.db import models
from django.core.validators import *

from django.db.models import ImageField, BooleanField, TextField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.models import User

import os
# Create your models here.


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
        blank = True,
        null = True

    )
    middleInitial = models.CharField(
        max_length=1,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z]$', message='Only letters can be input')],
        null = True,
        blank = True
    )
    lastName = models.CharField(
        max_length=50,
        default="",
        validators=[RegexValidator(regex='[a-zA-Z]$', message='Only letters can be input')],
        blank = True,
        null = True

    )
    gender = models.CharField(
        max_length=10,
        default="",
        blank = True,
        null = True
    )
    # Company field
    name = models.CharField(
        max_length=50,
        default="",
        blank = True,
        null = True

    )
    details = models.CharField(
        max_length=500,
        default="",
        null = True,
        blank = True
    )
    # Common field
    phoneNumber = PhoneNumberField(null = True,
        blank = True)
    email = models.EmailField(default="")
    def __str__(self):
        return str(self.user)
    def email(self):
        return self.user.email
    def is_admin(self):
        return self.user.is_staff
    def date_joined(self):
        return self.user.date_joined

class Skill(models.Model):
    skillName = TextField(primary_key = True)

    def __str__(self):
        return self.skillName

class UserSkill(models.Model):
    user = models.ForeignKey(ProfileInfo)
    skill = models.ForeignKey(Skill)

class Match(models.Model):
    user_1 = models.ForeignKey(ProfileInfo, related_name='company',on_delete=models.CASCADE)
    user_2 = models.ForeignKey(ProfileInfo, related_name='freelancer',on_delete=models.CASCADE)
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
