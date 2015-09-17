from django.core.urlresolvers import resolve

from django.test import TestCase
from django.test.client import RequestFactory

from artisthub.views import *


class TestArtistHubViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_artisthub_root_resolves_to_artisthub_home(self):
        request = self.factory.get('/artisthub/')
        response = artisthub_home(request)
        self.assertIn('bio-1', response.content, msg="bio-1 id not found in response.content")

    def test_artisthub_root_resolves_to_artist_profile(self):
        request = self.factory.get('/artisthub/')
        response = artisthub_home(request)
        self.assertIn('bio-1', response.content, msg="bio-1 id not found in response.content")