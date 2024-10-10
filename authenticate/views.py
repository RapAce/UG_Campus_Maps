from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def index(request):
    if request.method == "POST":
     usern=  request.POST.get("username")
     passw = request.POST.get("pass")
     user = authenticate(username=usern,password=passw)
     if user is not None:
         login(request,user)
         return redirect("home")



    context ={}
    return render(request, "authenticate/index.html", context)

def out(request):
    logout(request)
    return redirect("index")
