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
        self.assertIn('Welcome to the ArtistHub', response.content, msg="Did not find welcome message in response.content")

#    def test_artisthub_profile_links_resolve_to_artist_profile(self):
#        request = self.factory.get('/artisthub/')
#        response = artist_profile(request)
#        self.assertIn('Artist Name:', response.content, msg="Artist Name: not found in response.content")