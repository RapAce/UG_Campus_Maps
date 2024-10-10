from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import ExamEvent
from django.db.models import Q
from django.http import Http404
from .forms import ExamEventForm
from django.utils import timezone

def index(request):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    querysetdeleted = ExamEvent.objects.filter(date__lt=timezone.now())
    for m in querysetdeleted:
        m.delete()

    queryset = ExamEvent.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(coursetitle__icontains=query)|
            Q(coursecode__icontains=query)|
            Q(date__icontains=query)|
            Q(department__icontains=query)|
            Q(college__icontains=query)|
            Q(school__icontains=query)|
            Q(time__icontains=query)
        ).distinct()
    context = {
        "objectlist": queryset,
        "user": request.user,
    }
    return render(request, "examevents/index.html", context)

def create(request):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    form=ExamEventForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Operation Sucessfull")
        return redirect("examevents")
    context={
        "form":form,
    }
    return render(request, "examevents/create.html", context)

def delete(request,id=None):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    instance = ExamEvent.objects.get(id=id)
    instance.delete()
    return redirect("examevents")

def edit(request,id=None):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    instance = ExamEvent.objects.get(id=id)
    form = ExamEventForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item Saved")
        return redirect("examevents")
    context = {
        "form":form,
    }
    return render(request, "examevents/create.html", context)