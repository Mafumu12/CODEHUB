 
from django.contrib import admin
from django.urls import path
from .import views
 

urlpatterns = [
    path('home', views.home,name='home'),

    path('friends_suggestions', views.suggestions,name='friends_suggestions'),
    path('send_request', views.send_request,name='send_request'),
    path('friend_request/<str:profile_id>/', views.friend_requests,name='friend_request'),
    path('accept_request/<str:user_id>', views.accept_request,name='accept_request'),
    path('decline_request/<str:friend_request_id>/', views.decline_request,name='decline_request'),
    path('cancel_request', views.cancel_request,name='cancel_request'),
    path('remove_friend', views.remove_friend,name='remove_friend'),
    path('friends', views.friends,name='friends'),
    path('server', views.server,name='server'),
    path('home', views.create,name='create'),
]
