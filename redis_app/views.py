from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import EmployeesData
from django.http import JsonResponse
import json
import time

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_data(request):
    datas = EmployeesData.objects.values('name','salary','role','mobile','city','joined_date')[:90]
    final_data = []
    for data in datas:
        single_data ={
            'name':data['name'],
            'salary':data['salary'],
            'role':data['role'],
            'mobile':data['mobile'],
            'city':data['city'],
            'joined_date':data['joined_date']
        }
        final_data.append(single_data)
        time.sleep(0.01)
    return JsonResponse(final_data, safe=False)
