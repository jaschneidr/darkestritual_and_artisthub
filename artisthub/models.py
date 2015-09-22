from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    TYPE_AUTHOR = 'A'
    TYPE_MUSICIAN = 'M'
    TYPE_VISUALARTIST = 'V'

    TYPES = (
        (TYPE_AUTHOR, 'Author'),
        (TYPE_MUSICIAN, 'Musician'),
        (TYPE_VISUALARTIST, 'Visual Artist'),
    )

    user = models.OneToOneField(User)
    name = models.CharField(max_length=100, blank=True)
    profile_type = models.CharField(max_length=1, choices=TYPES, db_index=True)
    artist_name = models.CharField(max_length=140, blank=True, null=True)
    website = models.URLField(max_length=256, blank=True, null=True)
    bio = models.TextField(max_length=100000, blank=True, null=True)
    influences = models.TextField(max_length=100000, blank=True, null=True)

    def create_author(self):

        try:
            author = Author.objects.get(profile=self)
        except Author.DoesNotExist:
            if self.is_author():
                author = Author.objects.create(profile=self)
                author.save()

    def create_musician(self, subtype):

        try:
            musician = Musician.objects.get(profile=self)
        except Musician.DoesNotExist:
            if self.is_musician():
                musician = Musician.objects.create(profile=self, subtype=subtype)
                musician.save()

    def create_visual_artist(self):

        try:
            visual_artist = VisualArtist.objects.get(profile=self)
        except VisualArtist.DoesNotExist:
            if self.is_visual_artist():
                visual_artist = VisualArtist.objects.create(profile=self)
                visual_artist.save()

    def get_additional_artist_object(self):
        if self.is_author():
            return Author.objects.get(profile=self)
        if self.is_musician():
            return Musician.objects.get(profile=self)
        if self.is_visual_artist():
            return VisualArtist.objects.get(profile=self)

    def is_author(self):
        return self.profile_type == UserProfile.TYPE_AUTHOR

    def is_musician(self):
        return self.profile_type == UserProfile.TYPE_MUSICIAN

    def is_visual_artist(self):
        return self.profile_type == UserProfile.TYPE_VISUALARTIST


class Author(models.Model):
    profile = models.OneToOneField(UserProfile)
    pen_name = models.CharField(max_length=140, blank=True, null=True)
    dedication = models.TextField(max_length=5000, blank=True, null=True)


class VisualArtist(models.Model):
    profile = models.OneToOneField(UserProfile)
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

    musician = models.OneToOneField(Musician)
    members = models.TextField(max_length=256, blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)


class Instrumentalist(models.Model):

    musician = models.OneToOneField(Musician)
    instrument = models.CharField(max_length=256)


class Composer(models.Model):

    musician = models.OneToOneField(Musician)
    instruments_composed_for = models.TextField(max_length=1000, blank=True, null=True)


class Vocalist(models.Model):

    musician = models.OneToOneField(Musician)
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