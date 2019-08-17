from .forms import UserForm, UserProfileForm
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

import socket
import geocoder

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


# GeoSpoc Home page

class Home(TemplateView):
    template_name = 'home.html'
    # model = UserProfile


# Search method to get user profile based on Name, Web Address, Rating
def userlist(request):
    query = request.GET.get('search_object', None)
    search_term = UserProfile.objects.all()
    if query is not None:
        search_term = search_term.filter(
            Q(name__icontains=query) |
            Q(web_address__icontains=query) |
            Q(rating__icontains=query)
        )
    context = {
        'object_list': search_term
    }
    return render(request, 'user_list.html', context)


# user Registrations

def register(request):
    userform = UserForm()
    user_profile_form = UserProfileForm()
    if request.method == 'POST':
        userform = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)
        if userform.is_valid() and user_profile_form.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            profile = user_profile_form.save()
            profile.user = user
            profile.save()
        else:
            pass
    else:
        pass
    return render(request, 'register.html', {'userform': userform, 'user_profile_form': user_profile_form})


# log in user profile view

class Detail(LoginRequiredMixin, TemplateView):
    template_name = 'detail.html'
    model = UserProfile


# authenticated user login view method

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('geospoc_app:home'))
        else:
            return HttpResponse("your email or password is incorrect")
    return render(request, 'login.html', {})

# IP_Address view
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)

        return host_ip
    except:
        return 0

# Location View
def get_Host_location():
    g = geocoder.ip('me')
    ip_address = g.ip
    ip_location_city = g.city
    ip_location_country = g.country
    ip_location_state = g.state
    ip_location_postal = g.postal

    ip_location = ip_location_city + ',' + ip_location_state + ',' + ip_location_country + ',' + ip_location_postal
    return ip_address, ip_location



# Log Out view
@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('geospoc_app:home'))
