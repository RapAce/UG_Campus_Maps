from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import EventTyppe
from .forms import CategoryForm
from django.db.models import Q
from django.http import Http404

def index(request):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    queryset = EventTyppe.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(type__icontains=query)
        ).distinct()
    context = {
        "objectlist": queryset,
        "user": request.user
    }
    return render(request, "type/index.html", context)

def create(request):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    form=CategoryForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Operation Sucessfull")
        return redirect("types")
    context={
        "form":form,
    }
    return render(request, "type/create.html", context)

def delete(request,id=None):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    instance = EventTyppe.objects.get(id=id)
    instance.delete()
    return redirect("types")


def edit(request,id=None):
    if not request.user.is_authenticated:
        return redirect("authenticate")
    instance = EventTyppe.objects.get(id=id)
    form = CategoryForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item Saved")
        return redirect("types")
    context = {
        "form":form,
    }
    return render(request, "type/create.html", context)