from django.shortcuts import render
from PROFILEAPP.models import UserProfile
from PROFILEAPP.views import MyProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import FriendRequest,List_Of_Friends
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)
# Create your views here.

@login_required
def home(request):
    user = request.user

    try:
        user_profile = UserProfile.objects.get(name=user)
        context = {'user_profile': user_profile}
    except ObjectDoesNotExist:
        # Handle the case when the user's profile does not exist
        user_profile = None
        context = {'user_profile': user_profile}
        # You can also log an error message if needed
        

    return render(request,'home.html', context)


 
@login_required
def suggestions(request):
     

    user_profile = request.user.userprofile
    current_user_friends = List_Of_Friends.objects.get(friend=user_profile).friends.all()

     
    
    suggested_friends = UserProfile.objects.exclude(id__in=current_user_friends.values_list('id', flat=True))

     

    context = {'suggested_friends': suggested_friends}

   
    return render(request, 'friends.html', context)


@login_required
def send_request(request,*args,**kwargs):
    user = request.user
    payload = {}
    if request.method == "POST":
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            receiver = UserProfile.objects.get(pk = user_id)
            try:
                friend_requests = FriendRequest.objects.fiter(sender = user, receiver = receiver)

                try:
                    for request in friend_requests:
                        if request.is_active:
                            raise Exception("You already sent them afriend request.")
                    friend_request = FriendRequest(sender = user, receiver = receiver) 
                    friend_request.save() 
                    payload['response'] = "friend request sent"
                except Exception as e:
                    payload['response'] = str(e)
                    
            except FriendRequest.DoesNotExist:
                friend_request = FriendRequest(sender = user, receiver = receiver)
                friend_request.save()
                payload['response'] = "friend request sent."
            
            if payload['response'] == None:
                payload['response'] = "something went wrong."
    else:
        payload['response'] ="unable to send friend request."        

    return HttpResponse(json.dumps(payload),content_type = "application/json")
                  

@login_required
def friend_requests(request,profile_id):

     context = {}
     user =request.user
     user_account =  MyProfile.objects.get(pk = profile_id)
     if user_account == user:
         friend_requests = FriendRequest.objects.filter(receiver = user_account, is_active=True )
         context['friend_requests'] = friend_requests
     else:
         return HttpResponse('you cant view another users friend requests.')          

     return render(request)


@login_required
def accept_request(request,*args,**kwargs):
    user = request.user
    payload = {}
    if request.method == "GET":
        request_id = kwargs.get("request_id")
        if request_id:
            friend_request = FriendRequest.objects.get(pk = request_id)
            if friend_request.receiver == user:
                if friend_request:
                    friend_request.accept()
                    payload['response'] = "friend request accepted"
                else:
                    payload['response'] = "something went wrong"
            else:
                payload['response'] = "That is not you"
        else:
            payload['response'] = "Unable to accept that friend request."
    else:
    
     return HttpResponse(json.dumps(payload),content_type = "application/json")

@login_required
def decline_request(request,*args,**kwargs):
    user = request.user
    payload = {
    }
    if request.method == "GET":
        friend_request_id = kwargs.get("friend_request_id")
        if friend_request_id:
           friend_request = FriendRequest.objects.get(pk = friend_request_id)
           if friend_request.receiver == user:
               if friend_request:
                   friend_request.decline()
                   payload['response'] = "friend request decline" 
               else:
                   payload['response'] = "something went wrong."
           else: 
               payload['response'] = "that is not your friend request to decline"

        else:
            payload['response'] = "Unable to decline that friend request"
    HttpResponse(json.dumps(payload),content_type = "application/json")


def remove_friend(request,*args,**kwargs):
    user = request.user
    payload = {

    }
    if request.method == "POST":
        user_id = request.POST.get("receiver_user_id")
        if user_id:
          try:
              removee = UserProfile.objects.get(pk=user_id)
              friend_list = List_Of_Friends.objects.get(user = user)
              friend_list.unfriend(removee)
              payload['response'] = "successfully removed that friend "

          except Exception as e:
              payload['response'] = f"something went wrong: {str(e)}"
        else:
              payload['response'] = "there was an error. Unable to remove that friend. "
    return HttpResponse(json.dumps(payload), content_type = "application/json")

@login_required
def cancel_request(request,*args,**kwargs):
    user = request.user
    payload ={}
    if request.method == "POST":
        user_id =request.POST.GET("request_user_id")
        if user_id:
            receiver = UserProfile.objects.get(pk =user_id)
            try:
                friend_requests = FriendRequest.objects.filter(sender=user, receiver = receiver, is_active=True)
            except Exception as e:
                payload['response'] = "friend request does not exist."

                if len(friend_requests) > 1:
                    for request in friend_requests:
                        request.cancel()
                    payload['response'] = "friend resquet cancelled."
                else:
                    friend_requests.first().cancel()
                    payload['response'] ="friend request cancelled."
        else:
          payload['response'] ="unable to cancel friend request."  

    return HttpResponse(json.dumps(payload),content_type="application/json")      


@login_required
def friends(request,*args,**kwargs):

    context ={}
    user = request.user
    if user.is_authenticated:
        user_id = kwargs.get("user_id")
        if user_id:
            try:
                this_user = UserProfile.objects.get(pk = user_id)
                context['this_user'] = this_user
            except UserProfile.DoesNotExist:
                return HttpResponse(" That user does not esist  ")
            try:
                friend_list = List_Of_Friends.objects.get(user= this_user)
            except List_Of_Friends.DoesNotExist:
                return HttpResponse("could not find friendlist.")
            
            if user != this_user:
                if not user in friend_list.all():
                    return HttpResponse("you must be friends to view")

            friends = []
            auth_user_friend_list =List_Of_Friends.objects.get(user = user)
            for friend in friend_list.friends.all():
                friends.append((friend,auth_user_friend_list.mutual_friend(friend)))
            context['friends'] = friends       
    
    else:
        return HttpResponse("you have to be friends")
    return render(request,'friends.html')


def server(request):
    return render(request,'server.html')

def create(request):
    return render(request,'create-server.html')
























 

