from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from event.models import Event
from examevent.models import ExamEvent
from .serializers import EventSerializer,ExamEventSerializer
from django.utils import timezone

def index(request):
    context = {}
    return render(request, "api/index.html", context)

@api_view(['GET',])
def EventList(request):
    querysetdeleted = Event.objects.filter(enddate__lt=timezone.now())
    for m in querysetdeleted:
        m.delete()
    if request.method=="GET":
        stocks=Event.objects.all()
        serializer=EventSerializer(stocks,many=True)
        return Response(serializer.data)

@api_view(['GET',])
def Eventdetail(request,id=None):
    if request.method == "GET":
        instance=Event.objects.get(id=id)
        serializer=EventSerializer(instance,many=False)
        return Response(serializer.data)

@api_view(['GET',])
def ExamEventList(request):
    querysetdeleted = ExamEvent.objects.filter(date__lt=timezone.now())
    for m in querysetdeleted:
        m.delete()
    if request.method=="GET":
        stocks=ExamEvent.objects.all()
        serializer=ExamEventSerializer(stocks,many=True)
        return Response(serializer.data)

@api_view(['GET',])
def ExamEventdetail(request,id=None):
    if request.method == "GET":
        instance=ExamEvent.objects.get(id=id)
        serializer=ExamEventSerializer(instance,many=False)
        return Response(serializer.data)