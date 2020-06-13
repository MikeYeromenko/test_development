from django.urls import resolve
from rest_framework.test import APITestCase


from albums.models import Album, Track
from solos.models import Solo


class SoloAPITestCase(APITestCase):
    def setUp(self):
        self.giant_steps = Album.objects.create(name='Giant Steps', slug='giant-steps')

        self.mr_pc = Track.objects.create(name='Mr. PC', slug='mr-pc', album=self.giant_steps)

        self.drum_solo = Solo.objects.create(
            instrument='drums', artist='Buddy Rich',
            track=self.mr_pc, slug='buddy-rich', start_time='2:12')

        self.dirty_song = Solo.objects.create(
            instrument='drums', artist='XXX',
            track=self.mr_pc, slug='xxx', start_time='0:12')

    def test_list_solos(self):
        """
        Test if list of solos is returned
        """
        response = self.client.get('/api/solos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['instrument'], self.dirty_song.instrument)
        self.assertEqual(response.data[0]['track'], 'http://testserver/api/tracks/1/')
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[1]['url'], 'http://testserver/api/solos/1/')

    def test_create_solo(self):
        """
        Test that we can create Solo
        """
        post_data = {
            'track': '/api/tracks/1/',
            'artist': 'John Coltrane',
            'instrument': 'saxophone',
            'start_time': '0:24',
            'end_time': '3:21'
        }

        response = self.client.post('/api/solos/', data=post_data, format='json')
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data, {
            'url': 'http://testserver/api/solos/3/',
            'slug': 'john-coltrane',
            'track': 'http://testserver/api/tracks/1/',
            'artist': 'John Coltrane',
            'instrument': 'saxophone',
            'start_time': '0:24',
            'end_time': '3:21'
        })

    def test_url_for_solos(self):
        """
        Test if url exists, uses correct ViewSet
        """
        route = resolve('/api/solos/')
        self.assertEqual(route.func.__name__, 'SoloViewSet')
        self.assertEqual(route.url_name, 'solo-list')
