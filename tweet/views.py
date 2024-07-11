from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect,get_object_or_404
from .models import Tweet
from .forms import TweetForm
# Create your views here.
def index(request):
    return render(request, "index.html")


def tweet_list(request):
    tweet = Tweet.objects.all().order_by("-created_at")
    return render(request,"tweet_list.html",{"tweets":tweet})

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



def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request,"tweet_confirm_delete.html",{"tweet":tweet})

