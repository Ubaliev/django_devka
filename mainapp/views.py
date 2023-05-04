from rest_framework.viewsets import ModelViewSet

from mainapp.models import(
    Company, Job, Events, Video,
)

from mainapp.serializers import(
    CompanySerializer, JobSerializer, 
    EventsSerializer, VideoSerializer,
)

class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class JobView(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class EventsView(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer