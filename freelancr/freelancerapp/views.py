from django.shortcuts import render, render_to_response, redirect, loader
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    """
    Rendering the homepage for our various users: Admins, Patients/Doctors/Nurses (non-Admins), and
    AnonymousUsers - users who are not logged in.

    The display of this is different for each of the above groups.
    """
    # Is the current user logged in?
    #if request.user.is_authenticated():
    return render(request, 'freelancerapp/index.html')


