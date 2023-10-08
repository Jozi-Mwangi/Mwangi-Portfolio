from django.shortcuts import render
from .models import *
from .serializer import *

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework import status

# Create your views here.
# class ReactView(APIView):
#     def get(self, request):
#         output = [{
#             "job_title": output.job_title,
#             "job_description":output.job_description
#         }
#         for output in WebsiteExamples.objects.all()]

#         return Response(output)
    
#     def post(self, request):
#         serializer = WebsiteExamplesSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        
#     def delete (self, request, pk):
#         try:
#             portfolio_project = WebsiteExamples.objects.get(pk=pk)
#             portfolio_project.delete()
#             return Response(status=status.HTTP_200_OK)
#         except WebsiteExamples.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
                    

@api_view(["GET","POST", "DELETE"])
def portfolio_data(request):
    output = [{
            "job_id":output.job_id,
            "job_title": output.job_title,
            "job_description":output.job_description
        }
        for output in WebsiteExamples.objects.all()]
    
    if request.method == "GET":
        return Response(output)
    
    if request.method == "POST":
        try:
            serializer = WebsiteExamplesSerializer(data=output)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            return Response(status=status.HTTP_417_EXPECTATION_FAILED)

    if request.method == "DELETE":
        try:
            job_id = request.data.get("job_id")
            data_to_delete = WebsiteExamples.objects.get(pk=job_id)
            data_to_delete.delete()
            return Response(status=status.HTTP_200_OK)
        except WebsiteExamples.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
