from django.shortcuts import render
from rest_framework import viewsets, mixins

from albums.models import Album, Track
from albums.serializers import AlbumSerializer, TrackSerializer, SoloSerializer
from solos.models import Solo


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class SoloViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = SoloSerializer
    queryset = Solo.objects.all()

