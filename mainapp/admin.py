from django.contrib import admin

from mainapp.models import (Company,Job,Events,Video)

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Events)
admin.site.register(Video)

