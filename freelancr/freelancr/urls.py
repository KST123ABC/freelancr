"""freelancr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^registration/$', views.register, name='registration'),

    url(r'^login/$', views.login, name='login'),

    url(r'^logout/$', views.logout, name='logout'),

    url(r'^freelancer/$', views.freelancer, name='freelancer'),

    url(r'^freelancer_info/$', views.freelancer_info, name='freelancer_info'),

    url(r'^skills/$', views.skills, name='skills'),

    url(r'^like/$', views.like, name='like'),

    url(r'^super_like/$', views.super_like, name='super_like'),

    url(r'^company/$', views.company, name='company'),

    url(r'^company_info/$', views.company_info, name='company_info'),

    url(r'^swipe_left/$', views.swipe_left, name='swipe_left'),

    url(r'^swipe_right/$', views.swipe_right, name='swipe_right'),
]
