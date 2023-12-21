from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import login,authenticate,logout
from django.contrib import messages

# Create your views here.


def userlogin(request):

    if request.method == 'POST':
        username= request.POST.get('username',None)
        password= request.POST.get('password',None)
        user =authenticate(request,username=username,password=password)
        if user is not  None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
            return render(request,'login.html')
    else:
        context={'user':request.user}
             

    return render(request,'login.html',context)

def usersignin(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            #to log the user in 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request,username= username,password = password)
            login(request,user)
            return redirect('createprofile')
    else:
      form = UserCreationForm()
    context = {'form':form}
    return render(request,'signin.html',context)


    

def userlogout(request):
    logout(request)
    return redirect('login')