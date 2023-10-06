from django.db import models

# Create your models here.
class WebsiteExamples(models.Model):
    job_title = models.CharField(max_length=30)
    job_description = models.TextField()
    # job_images = models.ImageField()
