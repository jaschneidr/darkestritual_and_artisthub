from django.core.urlresolvers import resolve

from django.test import TestCase
from django.test.client import RequestFactory


from .factories import UserProfileFactory, MusicianFactory
from .models import (
    UserProfile, Author, Musician, VisualArtist,
    Band, Composer, Instrumentalist, Vocalist
)

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
        self.profile.profile_type = UserProfile.TYPE_MUSICIAN
        self.assertTrue(self.profile.is_musician(), msg='With criteria met, a musician type profile returns false with .is_musician() method.')

    def test_profile_is_musician_returns_false_when_false(self):
        for profile_type in [option[0] for option in UserProfile.TYPES if option[0] not in UserProfile.TYPE_MUSICIAN]:
            self.profile.profile_type = profile_type
            self.assertFalse(self.profile.is_musician(), msg='Without criteria met, a profile object with type "{0}" returns true when .is_musician() is called.'.format(profile_type))

    def test_profile_is_author_returns_true_when_true(self):
        self.profile.profile_type = UserProfile.TYPE_AUTHOR
        self.assertTrue(self.profile.is_author(), msg='With criteria met, an author type profile returns false with the .is_author() method.')

    def test_profile_is_author_returns_false_when_false(self):
        for profile_type in [option[0] for option in UserProfile.TYPES if option[0] not in UserProfile.TYPE_AUTHOR]:
            self.profile.profile_type = profile_type
            self.assertFalse(self.profile.is_author(), msg='Without criteria met, a profile object with type "{0}" returns true when .is_author() is called.'.format(profile_type))

    def test_profile_is_visual_artist_returns_true_when_true(self):
        self.profile.profile_type = UserProfile.TYPE_VISUALARTIST
        self.assertTrue(self.profile.is_visual_artist(), msg='With criteria met, a visual artist type profile returns false when .is_visual_artist() method should return true.')

    def test_profile_is_visual_artist_returns_false_when_false(self):
        for profile_type in [option[0] for option in UserProfile.TYPES if option[0] not in UserProfile.TYPE_VISUALARTIST]:
            self.profile.profile_type = profile_type
            self.assertFalse(self.profile.is_visual_artist(), msg='Without criteria met, a profile object with type "{0}" returns true when .is_visual_artist() is called.'.format(profile_type))

    def test_profile_create_musician_with_conditions_met(self):
        self.profile.profile_type = UserProfile.TYPE_MUSICIAN
        self.profile.create_musician(subtype=Musician.SUBTYPE_BAND)
        self.assertTrue(Musician.objects.get(profile=self.profile), msg='Musician object does not save with conditions met.')

    def test_profile_create_musician_without_is_musician_condition_met(self):
        for profile_type in [option[0] for option in UserProfile.TYPES if option[0] not in UserProfile.TYPE_MUSICIAN]:
            self.profile.profile_type = profile_type
            self.profile.create_musician(subtype=Musician.SUBTYPE_VOCALIST)
            with self.assertRaises(Musician.DoesNotExist, msg='With profile_type "{0}", a musician object created anyway when it should not have.'.format(profile_type)):
                Musician.objects.get(profile=self.profile)

    def test_profile_create_author_with_conditions_met(self):
        self.profile.profile_type = UserProfile.TYPE_AUTHOR
        self.profile.create_author()
        self.assertTrue(Author.objects.get(profile=self.profile), msg='Author object does not save with conditions met.')

    def test_profile_create_author_without_is_musician_condition_met(self):
        for profile_type in [option[0] for option in UserProfile.TYPES if option[0] not in UserProfile.TYPE_AUTHOR]:
            self.profile.profile_type = profile_type
            self.profile.create_author()
            with self.assertRaises(Author.DoesNotExist, msg='With profile_type "{0}", an author object created anyway when it should not have.'.format(profile_type)):
                Author.objects.get(profile=self.profile)

    def test_profile_create_visual_artist_with_conditions_met(self):
        self.profile.profile_type = UserProfile.TYPE_VISUALARTIST
        self.profile.create_visual_artist()
        self.assertTrue(VisualArtist.objects.get(profile=self.profile), msg='VisualArtist object does not save with conditions met.')

    def test_profile_create_visual_artist_without_is_musician_condition_met(self):
        for profile_type in [option[0] for option in UserProfile.TYPES if option[0] not in UserProfile.TYPE_VISUALARTIST]:
            self.profile.profile_type = profile_type
            self.profile.create_visual_artist()
            with self.assertRaises(VisualArtist.DoesNotExist, msg='With profile_type "{0}", a VisualArtist object created anyway when it should not have.'.format(profile_type)):
                VisualArtist.objects.get(profile=self.profile)

    # Test get_additional_artist_objects
                # 1 Test that it does not return an incorrect additional artist object for the profile type
                # 2 Test that it _does_ return the correct additional artist object
    def test_get_additional_artist_object_musician(self):
        self.profile.profile_type = UserProfile.TYPE_MUSICIAN
        self.profile.create_musician(subtype=Musician.SUBTYPE_BAND)
        self.profile.get_additional_artist_object()
        musician = False
        try:
            musician = Musician.objects.get(profile=self.profile)
        except Musician.DoesNotExist:
            pass

        self.assertTrue(musician, msg='With profile_type TYPE_MUSICIAN, userprofile.get_additional_artist_object() does not return a musician object.')




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
