# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='MusicAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('release_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileSubtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=140, null=True, blank=True)),
                ('website', models.URLField(max_length=256, null=True, blank=True)),
                ('bio', models.TextField(max_length=100000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('profiletype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='artisthub.ProfileType')),
                ('pen_name', models.CharField(max_length=140, null=True, blank=True)),
                ('dedication', models.TextField(max_length=5000, null=True, blank=True)),
            ],
            bases=('artisthub.profiletype',),
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('profilesubtype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='artisthub.ProfileSubtype')),
                ('types_of_pieces', models.TextField(max_length=1000, null=True, blank=True)),
            ],
            bases=('artisthub.profilesubtype',),
        ),
        migrations.CreateModel(
            name='Instrumentalist',
            fields=[
                ('profilesubtype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='artisthub.ProfileSubtype')),
                ('instrument', models.CharField(max_length=256)),
            ],
            bases=('artisthub.profilesubtype',),
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('profiletype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='artisthub.ProfileType')),
                ('members', models.TextField(max_length=256, null=True, blank=True)),
            ],
            bases=('artisthub.profiletype',),
        ),
        migrations.CreateModel(
            name='SingerSongwriter',
            fields=[
                ('profilesubtype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='artisthub.ProfileSubtype')),
                ('genre', models.CharField(max_length=60, null=True, blank=True)),
            ],
            bases=('artisthub.profilesubtype',),
        ),
        migrations.CreateModel(
            name='VisualArtist',
            fields=[
                ('profiletype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='artisthub.ProfileType')),
                ('dedication', models.TextField(max_length=5000, null=True, blank=True)),
            ],
            bases=('artisthub.profiletype',),
        ),
        migrations.CreateModel(
            name='Vocalist',
            fields=[
                ('profilesubtype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='artisthub.ProfileSubtype')),
                ('range', models.CharField(max_length=60, null=True, blank=True)),
            ],
            bases=('artisthub.profilesubtype',),
        ),
        migrations.AddField(
            model_name='profiletype',
            name='profile',
            field=models.ForeignKey(related_name='artist_types', to='artisthub.UserProfile'),
        ),
        migrations.AddField(
            model_name='profilesubtype',
            name='type',
            field=models.ForeignKey(related_name='subtypes', to='artisthub.ProfileType'),
        ),
        migrations.AddField(
            model_name='audioupload',
            name='album',
            field=models.ForeignKey(related_name='songs', to='artisthub.MusicAlbum'),
        ),
        migrations.AddField(
            model_name='musicalbum',
            name='musician',
            field=models.ForeignKey(related_name='artists_albums', to='artisthub.Musician'),
        ),
        migrations.AddField(
            model_name='audioupload',
            name='musician',
            field=models.ForeignKey(related_name='artists_songs', to='artisthub.Musician'),
        ),
    ]
