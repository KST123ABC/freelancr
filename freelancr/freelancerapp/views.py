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
    if request.user.is_authenticated():
        return render(request, 'accounts/home.html')

"""
def user_login(request):
    """
"""
    Where the login information is being authenticated for all possible users.

    This was not named 'login' because that would conflict with built-in Django functions.
    """"""
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/dashboard')
            else:
                messages.info(request, "This account has been disabled. Please contact the administrator if you think this is an error.")
                return render(request, 'accounts/login.html', request.POST)
        else:
            messages.info(request, "Invalid details supplied. Please try again.")
            return render(request, 'accounts/login.html', request.POST)
    else:
        if request.user.is_active:
            return redirect('/dashboard')
        else:
            return render_to_response('accounts/login.html', {}, context)

@login_required
def log_away(request):
""""""
    Essentially just an expansion on the basic logout() functionality, this will
    both log out a user and send them to the homepage.

    Login_required is turned on because logging out someone not logged in would cause issues.

    This was not named 'logout' because that would conflict with built-in Django functions.
    """"""
    logout(request)
    return redirect('/')


def registration(request):
    """"""
    Where the patient's form is being used to create a new instance of the patient
    """"""

    if request.method == 'POST':
        user_form = RegistrationForm(request.POST, prefix="user")
        if user_form.is_valid():
            user = user_form.save_m2m()
            user.save()
            return redirect('/')
        else:
            return render(request, 'accounts/reg_form.html', {'form1': user_form})

    else:
        user_form = RegistrationForm(prefix="user")
        return render(request, 'accounts/reg_form.html', {'form1': user_form})

@login_required
def profile(request):
    """"""
    Where the profile information is being rendered for display to the patient.

    Only viewable by the patient.
    """"""

    context = dict()

    if request.method == 'POST':
        if len(request.POST) > 1:
            return HttpResponse("test")
        # This happens otherwise, i.e. load that empty form
        else:
            template = loader.get_template("accounts/profileupdate.html")
            user_form = UserForm
            context = {'form': user_form}
            return HttpResponse(template.render(context, request))

    user = request.user

    if hasattr(user, "freelancer"):
        context['based'] = 'base.html'
        context['Curr'] = Freelancer.objects.filter(user=user)
        return render(request, 'accounts/profile.html', context)
    if hasattr(user, "company"):
        context['based'] = 'base.html'
        context['Curr'] = Company.objects.filer(user=user)
        return render(request, 'accounts/profile.html', context)
    else:
        return HttpResponse("You don't have permission to be here!")

class FreelancerUpdate(UpdateView):
    """"""
    Updates the currently logged-in patient's profile.

    Only viewable by patients.
    """"""

    form_class = FreelancerUpdateForm
    model = Freelancer
    template_name = 'freelancer_update_form.html'
    success_url = '/profile'

    def get_object(self, queryset=None):
        obj = Freelancer.objects.get(id=self.request.user.patient.id)
        return obj


class CompanyUpdate(UpdateView):
    """"""
    Updates the currently logged-in patient's profile.

    Only viewable by patients.
    """"""

    form_class = CompanyUpdateForm
    model = Company
    template_name = 'company_update_form.html'
    success_url = '/profile'

    def get_object(self, queryset=None):
        obj = Company.objects.get(id=self.request.user.patient.id)
        return obj

class swipe_left(UpdateView):
    model = CardStack
    template_name = 'dashboard.html'
    success_url = 'dashboard.html'

class swipe_right(UpdateView):
    model = CardStack
    template_name = 'dashboard.html'
    success_url = 'dashboard.html'

"""