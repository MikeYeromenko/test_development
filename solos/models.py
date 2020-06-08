from django.db import models
from django.urls import reverse

from albums.models import Track


class Solo(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='solos')
    artist = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('solos:solo_detail_view', kwargs={
            'album': self.track.album.slug,
            'artist': self.slug,
            'track': self.track.slug
        })

    def get_duration(self):
        """
        Returns Solos duration in format '1:04 - 2:05' or empty string
        """
        return f'{self.start_time}-{self.end_time}' if self.start_time and self.end_time else ''

    class Meta:
        ordering = ['track', 'start_time']
        verbose_name_plural = 'solos'
