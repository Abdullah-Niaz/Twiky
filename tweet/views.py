from .forms import BootstrapLoginForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import *
from .models import Tweet
from .forms import TweetForm,UserRegistrationFrom
# Create your views here.
def index(request):
    return render(request, "index.html")


def tweet_list(request):
    tweet = Tweet.objects.all().order_by("-created_at")
    return render(request,"tweet_list.html",{"tweets":tweet})

@login_required
def tweet_create(request):
    if request.method =="POST":
        tweet = TweetForm(request.POST,request.FILES)
        if tweet.is_valid():
            tweet = tweet.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
        pass
    else:
        form = TweetForm()
    return render(request,"tweet_form.html",{"form":form})


@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if(request.method == "POST"):
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        
        if(form.is_valid()):
            tweet = TweetForm.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list") 
        
    else:
        form = TweetForm()
    return render(request,"tweet_form.html",{"form":form})



@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet_confirm_delete.html", {"tweet": tweet})


class CustomLoginView(LoginView):
    authentication_form = BootstrapLoginForm
    template_name = 'login.html'  


def register(request):
    if request.method == "POST":
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            print("User registered and logged in successfully")  # Debug statement
            return redirect("tweet_list")
        else:
            print("Form is not valid")  # Debug statement
    else:
        form = UserRegistrationFrom()
    return render(request, "registration/register.html", {"form": form})
