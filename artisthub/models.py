import datetime
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    name = models.CharField(max_length=256, blank=False, null=True)


class ProfileType(models.Model):

    profile = models.ForeignKey('UserProfile', related_name='artist_types')
    artist_name = models.CharField(max_length=140, blank=True, null=True)
    website = models.URLField(max_length=256, blank=True, null=True)
    bio = models.TextField(max_length=100000, blank=True, null=True)


class ProfileSubtype(models.Model):

    name = models.CharField(max_length=100)
    type = models.ForeignKey('ProfileType', related_name='subtypes')


class Musician(ProfileType):

    members = models.TextField(max_length=256, blank=True, null=True)


class Author(ProfileType):

    pen_name = models.CharField(max_length=140, blank=True, null=True)
    dedication = models.TextField(max_length=5000, blank=True, null=True)


class VisualArtist(ProfileType):

    dedication = models.TextField(max_length=5000, blank=True, null=True)


class Instrumentalist(ProfileSubtype):

    instrument = models.CharField(max_length=256)


class Composer(ProfileSubtype):

    types_of_pieces = models.TextField(max_length=1000, blank=True, null=True)


class SingerSongwriter(ProfileSubtype):

    genre = models.CharField(max_length=60, blank=True, null=True)


class Vocalist(ProfileSubtype):

    range = models.CharField(max_length=60, blank=True, null=True)


class MusicAlbum(models.Model):

    name = models.CharField(max_length=256, blank=False)
    release_date = models.DateField(blank=True)
    musician = models.ForeignKey('Musician', related_name='artists_albums')
    # album_cover


class AudioUpload(models.Model):

    musician = models.ForeignKey('Musician', related_name='artists_songs')
    name = models.CharField(max_length=256, blank=False)
    album = models.ForeignKey('MusicAlbum', related_name='songs')
    # file = models.CharField(max_length=512)
