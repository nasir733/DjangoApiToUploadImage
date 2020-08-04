from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import FileView
urlpatterns = [
    path('upload/',FileView.as_view(),name='file-upload')
]
