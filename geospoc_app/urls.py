from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from geospoc_app import views

app_name = 'geospoc_app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/', views.Detail.as_view(), name='profile'),
    path('userprofiles/', views.userlist, name='userprofiles'),
]
