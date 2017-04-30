from django.shortcuts import render, render_to_response, redirect, loader
from django.http import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse


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

def user_login(request):
	if request.method == "POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        # Redirect to a success page.
	        messages.success(request, 'Login Success')
	        print("Login Success\n")
	        return HttpResponseRedirect('/freelancr')
	    else:
	        # Return an 'invalid login' error message.
	        messages.error(request, "This account has been disabled. Please contact the administrator if you think this is an error.")
	        print("Login Fail\n")
	        return HttpResponseRedirect('/freelancr/login')
	return render(request, 'freelancerapp/login.html')

def logoff(request):
	logout(request)
	print("Log off Success")
	return HttpResponseRedirect("/freelancr")