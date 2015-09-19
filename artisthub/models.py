import datetime
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    TYPE_AUTHOR = 'A'
    TYPE_VISUALARTIST = 'V'
    TYPE_MUSICIAN = 'M'

    TYPES = (
        (TYPE_AUTHOR, 'Author'),
        (TYPE_VISUALARTIST, 'Visual Artist'),
        (TYPE_MUSICIAN, 'Musician'),
    )

    user = models.OneToOneField(User)
    name = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=1, choices=TYPES, db_index=True)
    artist_name = models.CharField(max_length=140, blank=True, null=True)
    website = models.URLField(max_length=256, blank=True, null=True)
    bio = models.TextField(max_length=100000, blank=True, null=True)
    influences = models.TextField(max_length=100000, blank=True, null=True)


    def is_author(self):
        return self.type == UserProfile.TYPE_AUTHOR

    def is_visual_artist(self):
        return self.type == UserProfile.TYPE_VISUALARTIST

    def is_musician(self):
        return self.type == UserProfile.TYPE_MUSICIAN

    # def get_profile_type


class Author(UserProfile):

    pen_name = models.CharField(max_length=140, blank=True, null=True)
    dedication = models.TextField(max_length=5000, blank=True, null=True)


class VisualArtist(UserProfile):

    dedication = models.TextField(max_length=5000, blank=True, null=True)


class Musician(models.Model):

    SUBTYPE_BAND = 'B'
    SUBTYPE_COMPOSER = 'C'
    SUBTYPE_INSTRUMENTALIST = 'I'
    SUBTYPE_VOCALIST = 'V'

    SUBTYPES = (
        (SUBTYPE_BAND, 'Band'),
        (SUBTYPE_COMPOSER, 'Composer'),
        (SUBTYPE_INSTRUMENTALIST, 'Instrumentalist'),
        (SUBTYPE_VOCALIST, 'Vocalist'),
    )

    subtype = models.CharField(max_length=1, choices=SUBTYPES, db_index=True)

    profile = models.OneToOneField(UserProfile)
    genre = models.TextField(max_length=100, blank=True, null=True)

    def is_band(self):
        return self.profile.is_musician() and self.subtype == Musician.SUBTYPE_BAND

    def is_composer(self):
        return self.profile.is_musician() and self.subtype == Musician.SUBTYPE_COMPOSER

    def is_instrumentalist(self):
        return self.profile.is_musician() and self.subtype == Musician.SUBTYPE_INSTRUMENTALIST

    def is_vocalist(self):
        return self.profile.is_musician() and self.subtype == Musician.SUBTYPE_VOCALIST


class Band(models.Model):

    members = models.TextField(max_length=256, blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)


class Instrumentalist(models.Model):

    instrument = models.CharField(max_length=256)


class Composer(models.Model):

    instruments_composed_for = models.TextField(max_length=1000, blank=True, null=True)


class Vocalist(models.Model):

    range = models.CharField(max_length=60, blank=True, null=True)


class MusicAlbum(models.Model):

    name = models.CharField(max_length=256, blank=False)
    release_date = models.DateField(blank=True)
    musician = models.ForeignKey('Musician', related_name='artists_albums')
    # direct zipped file links (aac and mp3) to be added once infrastructure has been created
    # download_link_aac
    # download_link_mp3
    # album art


class AudioUpload(models.Model):

    musician = models.ForeignKey('Musician', related_name='artists_songs')
    name = models.CharField(max_length=256, blank=False)
    album = models.ForeignKey('MusicAlbum', related_name='songs')
    # mp3/aac audio file link to be added once infrastructure has been created
    # download_link_aac
    # download_link_mp3