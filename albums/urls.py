from django.urls import path, include
from rest_framework import routers


from albums.views import AlbumViewSet, TrackViewSet, SoloViewSet

# app_name = 'albums'

router = routers.DefaultRouter()
router.register('albums', viewset=AlbumViewSet, basename='album')
router.register('tracks', viewset=TrackViewSet, basename='track')
router.register('solos', viewset=SoloViewSet, basename='solo')


urlpatterns = [
    path('', include(router.urls)),
]
