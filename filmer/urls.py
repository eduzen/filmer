"""filmer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ht/", include("health_check.urls")),
    # path("v1", include("filmer.urls")),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
