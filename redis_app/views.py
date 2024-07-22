from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import EmployeesData
from django.http import JsonResponse
import json
import time

from django.core.cache import cache

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_data(request):
    cache_key = "employees_data"
    result_final = cache.get(cache_key)
    if not result_final:
        datas = EmployeesData.objects.values('name', 'salary', 'role', 'mobile', 'city', 'joined_date')[:90]
        result_final = []
        for data in datas:
            single_data = {
                'name': data['name'],
                'salary': data['salary'],
                'role': data['role'],
                'mobile': data['mobile'],
                'city': data['city'],
                'joined_date': data['joined_date']
            }
            result_final.append(single_data)
            time.sleep(0.01)
    cache.set(cache_key, result_final, timeout=60)  # Set cache timeout to 1 minute (60 seconds)
    return JsonResponse(result_final, safe=False)
