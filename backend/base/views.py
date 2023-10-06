from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response

# Create your views here.
class ReactView(APIView):
    def get(self, request):
        output = [{
            "job_title": output.job_title,
            "job_description":output.job_description
        }
        for output in WebsiteExamples.objects.all()]

        return Response(output)
    
    def post(self, request):
        serializer = WebsiteExamplesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)