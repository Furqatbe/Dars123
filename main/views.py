from dataclasses import dataclass
from django.shortcuts import render
from .serializer import *

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters
from .models import *
from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

# Create your views here.

@api_view(['GET'])
def GetTask(request):
    a = Task.objects.all()
    ser = TaskSer(a, many =True)
    return Response(ser.data)

@api_view(['GET'])
def Task_ID(request, pk):
    a = Task.objects.filter(id = pk) 
    if len(a) == 0:
        return Response({'status': "Bunday id yoq"})
    else:
        ser = TaskSer(a[0])
        return Response(ser.data)

@api_view(['POST'])
def Create_Task(request):
    name = request.POST.get('name')
    date = request.POST.get('date')

    a = Task.objects.create(name = name, date = date)
    ser = TaskSer(a)
    return Response(ser.data)

@api_view(['GET']) 
def Edit_Task(request, pk):
    a = Task.objects.grt(id = pk)
    a.status = True
    a.save()
    se = TaskSer()
    return Response(se.data)

@api_view(['GET'])
def TypeStatus(request):
    types = request.GET['type']
    if types:
        a = Task.objects.filter(status = True) 
    if types == False:
        a = Task.objects.filter(status = False)
    ser = TaskSer(a, many = True)
    return Response(ser.data)
from rest_framework import filters

@api_view(['GET'])
def GetSearch(request):
    search = request.GET['search']
    a = Task.objects.filter(name_icontains = search)
    ser = TaskSer(a, many = True)
    return Response(ser.data)
    


