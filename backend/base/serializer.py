from rest_framework import serializers
from . models import *

class WebsiteExamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteExamples
        fields = ["job_title", "job_description", "job_images", "job_id"]
