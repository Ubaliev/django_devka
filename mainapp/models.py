from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=127)
    logo = models.ImageField(upload_to='logos/', blank=True)
    description = models.TextField(verbose_name='описание')
    telegram = models.URLField(verbose_name='telegram')
    whatsapp = models.URLField(verbose_name='whatsapp')

    @property
    def events_amount(self):
        return self.events.count()

    @property
    def job_amount(self):
        return self.jobs.count()

    @property
    def video_amount(self):
        return self.videos.count()
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
    related_name='jobs')
    work = models.CharField(max_length=127)
    price = models.CharField(max_length=127)
    type_work = models.CharField(max_length=127)
    description = models.TextField(verbose_name='описание')
    telegram = models.CharField(max_length=127)
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=127)

class Events(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
    related_name='events')
    location = models.CharField(max_length=127)
    date = models.DateTimeField()
    website = models.URLField()
    registration = models.URLField()
    description = models.TextField(verbose_name='описание1')
    name = models.CharField(max_length=127)
    image = models.ImageField(upload_to='images')

class Video(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
    related_name='videos')
    date = models.DateTimeField()
    image_video = models.ImageField(upload_to='images1')
    name_video = models.CharField(max_length=127)



