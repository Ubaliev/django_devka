from rest_framework import serializers

from mainapp.models import(
    Company, Job, Events, Video,
)

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',  
            'work', 'price', 'type_work', 'description', 
            'telegram', 'email', 'phone',
        )

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = (
            'id', 'location', 
            'date', 'website', 'registration', 'description',
            'name', 'image',
        )

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'id', 'company', 'date', 'image_video', 'name_video',
        )


class CompanySerializer(serializers.ModelSerializer):
    jobs = JobSerializer(read_only=True, many=True)
    events = EventsSerializer(read_only=True, many=True)
    videos = VideoSerializer(read_only=True, many=True)
    class Meta:
        model = Company
        fields = ( 
            'id', 'name', 'logo', 'description', 'telegram', 
            'whatsapp', 'jobs', 'events', 'videos',
        )