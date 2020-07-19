from django.urls import path
from .views import hello_template, hello_render

urlpatterns = [
    path('hello/', hello_template),
    path('hello-render/', hello_render),
]