from django.core.urlresolvers import resolve

from django.test import TestCase
from django.test.client import RequestFactory


from .factories import UserProfileFactory, MusicianFactory
from .models import UserProfile, Musician

from artisthub.views import *


class TestArtistHubViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_artisthub_root_resolves_to_artisthub_home(self):
        request = self.factory.get('/artisthub/')
        response = artisthub_home(request)
        self.assertIn('Welcome to the ArtistHub', response.content, msg="Did not find welcome message in response.content")


class TestUserProfile(TestCase):

    def setUp(self):
        self.profile = UserProfileFactory()

    def test_profile_is_musician_returns_true_when_true(self):
        self.profile.type = UserProfile.TYPE_MUSICIAN
        self.assertTrue(self.profile.is_musician(), msg='With criteria met, a musician type profile returns false with .is_musician() method.')

    def test_profile_is_musician_returns_false_when_false(self):
        for profile_type in [option[0] for option in UserProfile.TYPES if option[0] not in UserProfile.TYPE_MUSICIAN]:
            self.profile.type = type
            self.assertFalse(self.profile.is_musician(), msg='Without criteria met, a profile object with type "{0}" returns true when .is_musician() is called.'.format(profile_type))

    def test_profile_is_author_returns_true_when_true(self):
        self.profile.type = UserProfile.TYPE_AUTHOR
        self.assertTrue(self.profile.is_author(), msg='With criteria met, an author type profile returns false with the .is_author() method.')

    def test_profile_is_author_returns_false_when_false(self):
        for profile_type in [option[0] for option in UserProfile.TYPES if option[0] not in UserProfile.TYPE_AUTHOR]:
            self.profile.type = type
            self.assertFalse(self.profile.is_author(), msg='Without criteria met, a profile object with type "{0}" returns true when .is_author() is called.'.format(profile_type))

    def test_profile_is_visual_artist_returns_true_when_true(self):
        self.profile.type = UserProfile.TYPE_VISUALARTIST
        self.assertTrue(self.profile.is_visual_artist(), msg='With criteria met, a visual artist type profile returns false when .is_visual_artist() method should return true.')

    def test_profile_is_visual_artist_returns_false_when_false(self):
        for profile_type in [option[0] for option in UserProfile.TYPES if option[0] not in UserProfile.TYPE_VISUALARTIST]:
            self.profile.type = type
            self.assertFalse(self.profile.is_visual_artist(), msg='Without criteria met, a profile object with type "{0}" returns true when .is_visual_artist() is called.'.format(profile_type))

class TestMusician(TestCase):

    def setUp(self):
        self.musician = MusicianFactory()

    def test_musician_is_band_returns_true_when_true(self):
        self.musician.subtype = Musician.SUBTYPE_BAND
        self.assertTrue(self.musician.is_band(), msg='With criteria met, a band subtyped musician object returns false when .is_band() is called.')

    def test_musician_is_band_returns_false_when_false(self):
        for subtype in [option[0] for option in Musician.SUBTYPES if option[0] not in Musician.SUBTYPE_BAND]:
            self.musician.subtype = subtype
            self.assertFalse(self.musician.is_band(), msg='Without criteria met, a musician object with subtype "{0}" returns true when .is_band() is called.'.format(subtype))

    def test_musician_is_composer_returns_true_when_true(self):
        self.musician.subtype = Musician.SUBTYPE_COMPOSER
        self.assertTrue(self.musician.is_composer(), msg='With criteria met, a composer subtyped musician object returns false when is_composer() is called.')

    def test_musician_is_composer_returns_false_when_false(self):
        for subtype in [option[0] for option in Musician.SUBTYPES if option[0] not in Musician.SUBTYPE_COMPOSER]:
            self.musician.subtype = subtype
            self.assertFalse(self.musician.is_composer(), msg='Without criteria met, a musician object with subtype "{0}" returns true when .is_composer() is called.'.format(subtype))

    def test_musician_is_instrumentalist_returns_true_when_true(self):
        self.musician.subtype = Musician.SUBTYPE_INSTRUMENTALIST
        self.assertTrue(self.musician.is_instrumentalist(), msg='With criteria met, an instrumentalist subtyped musician object returned false when .is_instrumentalist() was called.')

    def test_musician_is_instrumentalist_returns_false_when_false(self):
        for subtype in [option[0] for option in Musician.SUBTYPES if option[0] not in Musician.SUBTYPE_INSTRUMENTALIST]:
            self.musician.subtype = subtype
            self.assertFalse(self.musician.is_instrumentalist(), msg='Without criteria met, a musician object with subtype "{0}" returns true when .is_instrumentalist() is called.'.format(subtype))

    def test_musician_is_vocalist_returns_true_when_true(self):
        self.musician.subtype = Musician.SUBTYPE_VOCALIST
        self.assertTrue(self.musician.is_vocalist(), msg='With criteria met, a vocalist subtyped musician object returns false when .is_vocalist() is called.')

    def test_musician_is_vocalist_returns_false_when_false(self):
        for subtype in [option[0] for option in Musician.SUBTYPES if option[0] not in Musician.SUBTYPE_VOCALIST]:
            self.musician.subtype = subtype
            self.assertFalse(self.musician.is_vocalist(), msg='Without criteria met, a musician object with subtype "{0}" returns true when .is_vocalist() is called.'.format(subtype))
