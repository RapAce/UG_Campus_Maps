from rest_framework import serializers
from event.models import Event
from examevent.models import ExamEvent

class EventSerializer(serializers.ModelSerializer):
    venue_name = serializers.CharField(source='venue.name')  #venue is foreign key and .name is its attribute
    venue_address=serializers.CharField(source='venue.address')
    venue_latitude=serializers.FloatField(source='venue.latitude')
    venue_longitude=serializers.FloatField(source='venue.longitude')
    venue_phonenumber=serializers.CharField(source='venue.phonenumber')
    venue_openinghours=serializers.CharField(source='venue.openinghours')
    venue_type=serializers.CharField(source='venue.type')
    venue_imageurl=serializers.CharField(source='venue.imageurl')
    venue_indoormap=serializers.URLField(source='venue.indoormap')
    event_type=serializers.CharField(source='type.type')

    class Meta:
        model=Event
        fields=['id','name','venue_name','venue_address','venue_latitude','venue_longitude','venue_phonenumber','venue_openinghours','venue_type','venue_imageurl','venue_indoormap','description','startdate','enddate','starttime','endtime','timestamp','updated','event_type']
        # fields='__all__'
        #read_only_fields=['id']

class ExamEventSerializer(serializers.ModelSerializer):
    venue_name = serializers.CharField(source='venue.name')
    venue_address=serializers.CharField(source='venue.address')
    venue_latitude=serializers.FloatField(source='venue.latitude')
    venue_longitude=serializers.FloatField(source='venue.longitude')
    venue_phonenumber=serializers.CharField(source='venue.phonenumber')
    venue_openinghours=serializers.CharField(source='venue.openinghours')
    venue_type=serializers.CharField(source='venue.type')
    venue_imageurl=serializers.CharField(source='venue.imageurl')
    venue_indoormap = serializers.URLField(source='venue.indoormap')

    class Meta:
        model=ExamEvent
        fields=['coursetitle','coursecode','venue_name','venue_address','venue_latitude','venue_longitude','venue_phonenumber','venue_openinghours','venue_type','venue_imageurl','venue_indoormap','date','starttime','endtime','college','school','department','level']
        # fields='__all__'
        #read_only_fields=['id']