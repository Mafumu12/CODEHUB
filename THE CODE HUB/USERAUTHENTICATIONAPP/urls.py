 
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.userlogin,name='login' ),
    path('signup/',views.usersignin,name='signup' ),
    path('logout/',views.userlogout,name='logout' ),
]
