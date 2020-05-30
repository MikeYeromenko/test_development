from django.test import TestCase
from django.urls import resolve


from solos.views import index


class SolosURLsTestCase(TestCase):

    def test_root_url_uses_index_view(self):
        """
        Tests that the root of the site resolves to the correct
        view function
        """
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        root = resolve('/')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{root.func}')
        self.assertEqual(root.func, index)
