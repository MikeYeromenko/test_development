from rest_framework.test import APITestCase

from albums.serializers import SoloSerializer


class SoloSerializerTestCase(APITestCase):

    def test_validate(self):
        """
        Tests that SoloSerializer.validate() adds a slugged version of the artist attribute
        to the data
        """
        serializer = SoloSerializer()
        data = serializer.validate({'artist': 'Ray Brown'})
        self.assertEqual(data, {
            'artist': 'Ray Brown',
            'slug': 'ray-brown'
        })
