from django.shortcuts import render,redirect
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)


# Create your views here.


def AccountSettings(request):
    return render(request,'Account-Settings.html')


@login_required
def MyProfile(request):
    user = request.user

    try:
        user_profile = UserProfile.objects.get(name=user)
        context = {'user_profile': user_profile}
    except ObjectDoesNotExist:
        # Handle the case when the user's profile does not exist
        user_profile = None
        context = {'user_profile': user_profile}
        # You can also log an error message if needed

    return render(request, 'Profile-Settings.html',context)
     

@login_required
def CreateProfile(request):
    if request.method == 'POST':
      form = UserProfileForm(request.POST,request.FILES)
      if form.is_valid():
          profile = form.save(commit=False)
          profile.name = request.user
          profile.save()
          return redirect('home')
      else:
            messages.error(request,"Form is not valid.")
    else:
        form = UserProfileForm()
    context = {'form':form}
    return render(request,'create-profile.html',context)

@login_required
def EditProfile(request,profile_id):

 profile = UserProfile.objects.get(pk=profile_id)
 if request.user.userprofile == profile:
    if request.method == 'POST':
      form = UserProfileForm(request.POST,request.FILES,instance=profile)
      if form.is_valid():
          form.save()
          return redirect('profilesettings')
      else:
            messages.error(request,"Form is not valid.")
    else:
        form = UserProfileForm(instance=profile)
    context = {'form':form}
    return render(request,'edit-profile.html',context)
 

@login_required
def DeleteProfile(request,profile_id):
    profile = UserProfile.objects.get(pk=profile_id)
    if request.user.userprofile == profile:
        profile.delete()
        request.user.delete()
        return redirect('signup')

     


def MyAccount(request):
     
    return render(request,'MyAccount.html')




def userprofile(request):
    return render(request,'UserProfile.html')