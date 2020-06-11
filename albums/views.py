from django.shortcuts import render
from rest_framework import viewsets, mixins

from albums.models import Album
from albums.serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

