from django.db import models

# Create your models here.
class WebsiteExamples(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=30)
    job_description = models.TextField()
    job_images = models.ImageField(null=True, blank=True, upload_to="images")
