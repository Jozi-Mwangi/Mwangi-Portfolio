from django.shortcuts import render
from .models import *
from .serializer import *

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework import status

# Create your views here.
@api_view(["GET", "POST"])
def portfolio_data(request):
    output = [{
        "job_id": output.job_id,
        "job_title": output.job_title,
        "job_description": output.job_description,
        "job_images":output.job_images
    }
        for output in WebsiteExamples.objects.all()]

    if request.method == "GET":
        serializer = WebsiteExamplesSerializer(output, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        try:
            serializer = WebsiteExamplesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                print("success")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Failed")
            return Response({"error: ", str(e)},status=status.HTTP_417_EXPECTATION_FAILED)

@api_view(["GET", "PUT", "DELETE"])
def portfolio_project(request, pk):
    """
    Retrieving a Project
    """

    try:
        project = WebsiteExamples.objects.get(pk=pk)
    except WebsiteExamples.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WebsiteExamplesSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        # data = JSONParser().parse(request)
        serializer = WebsiteExamplesSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
