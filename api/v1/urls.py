from django.urls import path
from .spectacular.urls import urlpatterns as doc_urls
from drf_spectacular.views import SpectacularAPIView
app_name = 'v1'

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]

urlpatterns += doc_urls
