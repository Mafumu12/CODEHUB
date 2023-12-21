 
from django.contrib import admin
from django.urls import path
from .import  views

urlpatterns = [
    path('accountsettings/', views.AccountSettings,name='accountsettings'),
    path('createprofile/', views.CreateProfile,name='createprofile'),
    path('EditProfile/<str:profile_id>/', views.EditProfile,name='EditProfile'),
    path('DeleteProfile/<str:profile_id>/', views.DeleteProfile,name='DeleteProfile'),
    path('myaccount/', views.MyAccount,name='myaccount'),
    path('profilesettings/', views.MyProfile,name='profilesettings'),
    path('userprofile/', views.userprofile,name='userprofile')
]