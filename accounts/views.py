from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from .models import Message

# Create your views here.


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "The User does not exist!!")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.save()
            messages.success(request, "successfully login")
            return redirect("home")
        else:
            messages.error(request, "incorect name or password")
    return render(request, "register/login.html")


def logout(request):
    logout(request)
    return redirect("login")


def signup_view(request):
    if request.method == "GET":
        user_form = forms.signup_form()
        return render(request, "register/signup.html", {"user_form": user_form})
    else:
        user_form = forms.signup_form(request.POST)
        if user_form.is_valid():
            new_form = user_form.save(commit=False)
            new_form.set_password(user_form.cleaned_data["password"])
            new_form.save()
            messages.success(request, "seccessfully registered")
            return redirect("login")

    return render(request, "register/signup.html", {"user_form": user_form})

def message(request):
    message = Message.objects.all()
    unread = message.filter(is_read = False).count()
    context = {
        'messages':message,
        'new_message': unread
    }
    return render(request, 'message/message.html', context)

def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message.is_read == False:
        message.is_read == True
        message.save()
    context = {
        'message':message
    }    
    return render(request, '', context)
    
def account_profile(request):
    user_profile = UserProfile.objects.all()
    print(user_profile)
    return render(request, 'profile/ali.html')
    