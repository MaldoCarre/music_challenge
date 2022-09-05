from django import views
from django.urls import path
from .views import Band_or_artis_info
urlpatterns = [
    path("", Band_or_artis_info.as_view(), name='music_info'),
]
