from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Venue
from .forms import VenueForm
from django.db.models import Q
from django.http import Http404


def index(request):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    queryset = Venue.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query)|
            Q(address__icontains=query)|
            Q(phonenumber__icontains=query)|
            Q(type__icontains=query)

        ).distinct()
    context = {
        "objectlist": queryset,
        "user": request.user
    }
    return render(request, "venue/index.html", context)

def create(request):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    form=VenueForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Operation Sucessfull")
        return redirect("venues")
    context={
        "form":form,
    }
    return render(request, "venue/create.html", context)

def delete(request,id=None):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    instance = Venue.objects.get(id=id)
    instance.delete()
    return redirect("venues")

def edit(request,id=None):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    instance = Venue.objects.get(id=id)
    form = VenueForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item Saved")
        return redirect("venues")
    context = {
        "form":form,
    }
    return render(request, "venue/create.html", context)