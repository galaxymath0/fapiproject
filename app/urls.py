from django.contrib import admin
from django.urls import path
from . import views
import json
urlpatterns = [
   path('api' , views.index , name="api")
]
