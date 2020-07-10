from django.shortcuts import render
from django.http import HttpResponse
from authapp.forms import UserForm, UserProfileForm
#imports for login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'home/index.html')


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username') #gets the username refering to the name of html input
        password = request.POST.get('password') #same here
        #django checks and authenticates the login
        user = authenticate(username = username, password=password)

        if user: # if there is a user authenticated
            if user.is_active: #if this authenticated user is active
                login(request,user) #now login
                return render (request, 'home/index.html') #when logged in you send user somewhere
            
            else: #if user not active
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("SOMEONE TRIES LOGIN AND FAILED")
            print("username: {} and password{}".format(username,password))
            return HttpResponse("INVALID LOGIN OR PASSWORD")

    else:
        return render(request, 'authapp/login.html',{})



@login_required #meaning function below requires user to be loggedin to work
def user_logout(request):
    logout(request)
    return render (request, 'home/index.html')




def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save() #here we grab the form and saves to the database
            user.set_password(user.password) #here we hashe the password
            user.save() #here we save the hashed password to the database
        #add the custom user attributes we created to user
            profile = profile_form.save(commit=False) #we dont want to commit to the database yet bc it might have collisions and overwrite the user
            profile.user = user #sets a one to one relationship
        #check if picture was provided (or any type of file actually)
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.erros, profile_form.erros)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'authapp/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

