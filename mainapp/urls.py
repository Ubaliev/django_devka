from rest_framework.routers import DefaultRouter as DR

from mainapp.views import (
    CompanyView, JobView, EventsView, VideoView,
)

router = DR()

router.register('company', CompanyView)

router.register('job', JobView)

router.register('event', EventsView)

router.register('video', VideoView)

urlpatterns = []

urlpatterns += router.urls