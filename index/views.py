from django.shortcuts import render
from event.models import Event
from examevent.models import ExamEvent
from django.db.models import Q
from django.utils import timezone

def index(request):
    querysetdeleted = Event.objects.filter(enddate__lt=timezone.now())
    for m in querysetdeleted:
        m.delete()
    queryset = Event.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query)|
            Q(startdate__icontains=query)|
            Q(enddate__icontains=query)|
            Q(description__icontains=query)
        ).distinct()
    query2 = request.GET.get("q2")
    if query2:
        queryset = queryset.filter(startdate__lte=query2,enddate__gte=query2).distinct()
    context = {
        "objectlist": queryset,
    }
    return render(request, "index/index.html", context)

def details(request,id=None):
    instance = Event.objects.get(id=id)
    context={
        "obj":instance,
    }
    return render(request,"index/details.html",context)

def examindex(request):
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
            Q(college__icontains=query)|
            Q(school__icontains=query)|
            Q(department__icontains=query)
        ).distinct()

    query2 = request.GET.get("q2")
    if query2:
        queryset = queryset.filter(date=query2).distinct()
    context = {
        "objectlist": queryset,
    }
    return render(request, "index/examindex.html", context)

def examdetails(request,id=None):
    instance = ExamEvent.objects.get(id=id)
    context={
        "obj":instance,
    }
    return render(request,"index/examdetails.html",context)