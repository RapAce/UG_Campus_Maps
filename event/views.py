from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Event
from django.db.models import Q
from django.http import Http404
from .forms import EventForm
from django.utils import timezone

def index(request):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    querysetdeleted = Event.objects.filter(enddate__lt=timezone.now())
    for m in querysetdeleted:
        m.delete()
    queryset = Event.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)|
            Q(startdate__icontains=query)|
            Q(enddate__icontains=query)|
            Q(starttime__icontains=query)|
            Q(endtime__icontains=query)
        ).distinct()
    context = {
        "objectlist": queryset,
        "user": request.user,
    }
    return render(request, "events/index.html", context)

def create(request):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    form=EventForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Operation Sucessfull")
        return redirect("events")
    context={
        "form":form,
    }
    return render(request, "events/create.html", context)

def delete(request,id=None):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    instance = Event.objects.get(id=id)
    instance.delete()
    return redirect("events")

def edit(request,id=None):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    instance = Event.objects.get(id=id)
    form = EventForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item Saved")
        return redirect("events")
    context = {
        "form":form,
    }
    return render(request, "events/create.html", context)