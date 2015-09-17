from django.core.urlresolvers import resolve

from django.test import TestCase
from django.test.client import RequestFactory

from home.views import *


class TestDarkestRitualHomeViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_root_url_resolves_to_global_home_view(self):
        request = self.factory.get('/')
        response = global_home(request)
        self.assertIn('bio-1', response.content, msg="bio-1 id not found in response.content")

    def test_slash_music_url_resolves_to_global_music_view(self):
        request = self.factory.get('/music')
        response = global_music(request)
        self.assertIn('music-downloadable', response.content, msg="music-downloadable class not found in response.content")

    def test_slash_visual_url_resolves_to_global_visual_view(self):
        request = self.factory.get('/visual')
        response = global_visual(request)
        self.assertIn('visual-art', response.content, msg="visual-art class not found in response.content")