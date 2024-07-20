from django.urls import path
from . import views

urlpatterns = [
    path('get-data/', views.get_user_data, name="join_date"),
]