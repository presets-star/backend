from django.urls import path, include
from django.contrib import admin
app_name = "api"

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
    path('v1/', include('api.v1.urls', namespace='v1')),
]
