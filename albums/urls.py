from django.urls import path, include
from rest_framework import routers


from albums.views import AlbumViewSet


# app_name = 'albums'

router = routers.DefaultRouter()
router.register('albums', viewset=AlbumViewSet, basename='album')


urlpatterns = [
    path('', include(router.urls)),
]
