import datetime
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    TYPE_AUTHOR = 'A'
    TYPE_VISUALARTIST = 'V'
    TYPE_MUSICIAN = 'M'
    TYPE_BAND = 'B'

    TYPES = (
        (TYPE_AUTHOR, 'Author'),
        (TYPE_VISUALARTIST, 'Visual Artist'),
        (TYPE_MUSICIAN, 'Musician'),
        (TYPE_BAND, 'Band'),
    )

    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length = 1, choices = TYPES, db_index = True)
    artist_name = models.CharField(max_length=140, blank=True, null=True)
    website = models.URLField(max_length=256, blank=True, null=True)
    bio = models.TextField(max_length=100000, blank=True, null=True)


class Musician(UserProfile):

    genre = models.TextField(max_length=100, blank=True, null=True)


class Band(Musician):

    members = models.TextField(max_length=256, blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)


class Author(UserProfile):

    pen_name = models.CharField(max_length=140, blank=True, null=True)
    dedication = models.TextField(max_length=5000, blank=True, null=True)


class VisualArtist(UserProfile):

    dedication = models.TextField(max_length=5000, blank=True, null=True)


class Instrumentalist(Musician):

    instrument = models.CharField(max_length=256)


class Composer(Musician):

    instruments_composed_for = models.TextField(max_length=1000, blank=True, null=True)


class Vocalist(Musician):

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
