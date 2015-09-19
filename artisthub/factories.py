# encoding utf-8

import factory
import factory.django
from django.contrib.auth.models import User


from .models import UserProfile, Musician


class UserProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserProfile

    user = factory.SubFactory('artisthub.factories.UserFactory', profile=None)
    name = factory.Sequence(lambda n: u'FirstName{0}'.format(n))
    artist_name = factory.Sequence(lambda n: u'The Artist Now Known As {0}'.format(n))
    website = factory.Sequence(lambda n: u'http://www.{0}.com'.format(n))
    bio = factory.Sequence(lambda n: u'We are {0} times better than you would expect!'.format(n))
    influences = factory.Sequence(lambda n: u'We have {0} influences, so it would be hard to list them all.'.format(n))
    type = UserProfile.TYPE_MUSICIAN


class MusicianFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Musician

    profile = factory.SubFactory(UserProfileFactory)
    genre = u'Progressive Ambient Black Metal'
    subtype = Musician.SUBTYPE_BAND


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: u'User{0}'.format(n))
    first_name = factory.Sequence(lambda n: u'FirstName{0}'.format(n))
    last_name = factory.Sequence(lambda n: u'LastName{0}'.format(n))
    email = factory.LazyAttribute(lambda a: u'{0}@example.com'.format(a.last_name).lower())
    profile = factory.RelatedFactory(UserProfileFactory, 'user')