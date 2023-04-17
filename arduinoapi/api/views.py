from django.shortcuts import render
from .models import Config
from .serializers import ConfigSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
class ConfigView(viewsets.ViewSet):
    def create(self,request):
        serializer=ConfigSerializer(data=request.data)
        if serializer.is_valid():
               serializer.save()
               return Response({"msg":"data created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request):
        stu=Config.objects.all()
        serializer =ConfigSerializer(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        stu=Config.objects.filter(id=pk).first()
        if stu is None:
             return Response({"msg":"id not exist is not exist"},status=status.HTTP_404_NOT_FOUND)
        serializer=ConfigSerializer(stu)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
            stu=Config.objects.filter(id=pk).first()
            if stu is None:
                    return Response({"msg":"id not exist is not exist"},status=status.HTTP_404_NOT_FOUND)
            serializer=ConfigSerializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                    serializer.save()
                    return Response({"msg":"data partailly updated"})
               
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
