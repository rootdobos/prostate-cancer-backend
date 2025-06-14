"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.files import list_files
from .views.features import encode_slide_tiles
from .views.tiles import extract_tiles_from_slide, get_attention_scores, get_attention_tiles,get_tile

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('slides/', list_files, name='slides'),

    path('tiles/extract', extract_tiles_from_slide,
         name='extract_tiles_from_slide'),

    path('tiles/encode', encode_slide_tiles, name='encode_slide_tiles'),
    path('tiles/get_attention_scores',
         get_attention_scores, name='get_attention_scores'),
    path('tiles/get_attention_tiles', get_attention_tiles, name='get_attention_tiles'),
    path('tiles/get_tile', get_tile, name='get_tile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
