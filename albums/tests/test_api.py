from django.urls import resolve, reverse
from rest_framework.test import APITestCase


from albums.models import Album, Track


class InitialBaseTestCase(APITestCase):
    def setUp(self):
        self.kind_of_blue = Album.objects.create(
            name='Kind of Blue')
        self.a_love_supreme = Album.objects.create(
            name='A Love Supreme')
        self.bugle_call_rag = Track.objects.create(
            name='Bugle Call Rag', slug='bugle-call-rag',
            album=self.kind_of_blue)
        self.mr_pc = Track.objects.create(
            name='Mr. PC', slug='mr-pc', album=self.a_love_supreme)


class AlbumAPITestCase(InitialBaseTestCase):

    def test_list_albums(self):
        """
        Test that we can get a list of albums
        """
        response = self.client.get('/api/albums/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'A Love Supreme')
        self.assertEqual(response.data[1]['name'], 'Kind of Blue')
        self.assertEqual(response.data[1]['url'], 'http://testserver/api/albums/1/')

    def test_album_list_route(self):
        """
        Test that we've got routing set up for Albums
        """

        route = resolve('/api/albums/')
        self.assertEqual(route.func.__name__, 'AlbumViewSet')


class TrackAPITestCase(InitialBaseTestCase):

    def test_list_tracks(self):
        """
        Test that we can get a list of tracks
        """
        response = self.client.get('/api/tracks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Mr. PC')
        self.assertEqual(response.data[1]['url'], 'http://testserver/api/tracks/1/')

    def test_url_api_tracks(self):
        """
        Test that url exists and uses correct controller
        """
        route = resolve('/api/tracks/')
        self.assertEqual(route.func.__name__, 'TrackViewSet')
