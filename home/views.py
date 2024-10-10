from django.shortcuts import render,redirect
from django.http import Http404

def index(request):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    context = {
         "user":request.user
    }
    return render(request, "home/index.html", context)