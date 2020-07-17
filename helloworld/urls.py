from django.contrib import admin
from django.urls import path

from world.views import home, profile, profile_json, int_converter_view, debug_request

urlpatterns = [
    path('profile/<str:username>/',profile),
    path('profile-json/<str:username>/',profile_json),
    path('path/<str:int_data>/',int_converter_view),
    path('test-path', debug_request),
    path('', home),
]
