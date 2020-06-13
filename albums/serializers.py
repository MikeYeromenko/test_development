from django.utils.text import slugify
from rest_framework import serializers

from albums.models import Album, Track
from solos.models import Solo


class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'


class TrackSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Track
        fields = '__all__'


class SoloSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, data):
        """
        Creates slug for solo
        :param data: data for validation
        :return: slug for artist
        """
        data['slug'] = slugify(data['artist'])
        return data

    class Meta:
        model = Solo
        fields = '__all__'
        read_only_fields = ('slug', )

