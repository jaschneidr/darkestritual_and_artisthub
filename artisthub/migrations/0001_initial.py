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
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pen_name', models.CharField(max_length=140, null=True, blank=True)),
                ('dedication', models.TextField(max_length=5000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('members', models.TextField(max_length=256, null=True, blank=True)),
                ('established_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instruments_composed_for', models.TextField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instrumentalist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instrument', models.CharField(max_length=256)),
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
            name='Musician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtype', models.CharField(db_index=True, max_length=1, choices=[(b'B', b'Band'), (b'C', b'Composer'), (b'I', b'Instrumentalist'), (b'V', b'Vocalist')])),
                ('genre', models.TextField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('profile_type', models.CharField(db_index=True, max_length=1, choices=[(b'A', b'Author'), (b'V', b'Visual Artist'), (b'M', b'Musician')])),
                ('artist_name', models.CharField(max_length=140, null=True, blank=True)),
                ('website', models.URLField(max_length=256, null=True, blank=True)),
                ('bio', models.TextField(max_length=100000, null=True, blank=True)),
                ('influences', models.TextField(max_length=100000, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VisualArtist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dedication', models.TextField(max_length=5000, null=True, blank=True)),
                ('profile', models.OneToOneField(to='artisthub.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Vocalist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('range', models.CharField(max_length=60, null=True, blank=True)),
                ('musician', models.OneToOneField(to='artisthub.Musician')),
            ],
        ),
        migrations.AddField(
            model_name='musician',
            name='profile',
            field=models.OneToOneField(to='artisthub.UserProfile'),
        ),
        migrations.AddField(
            model_name='musicalbum',
            name='musician',
            field=models.ForeignKey(related_name='artists_albums', to='artisthub.Musician'),
        ),
        migrations.AddField(
            model_name='instrumentalist',
            name='musician',
            field=models.OneToOneField(to='artisthub.Musician'),
        ),
        migrations.AddField(
            model_name='composer',
            name='musician',
            field=models.OneToOneField(to='artisthub.Musician'),
        ),
        migrations.AddField(
            model_name='band',
            name='musician',
            field=models.OneToOneField(to='artisthub.Musician'),
        ),
        migrations.AddField(
            model_name='author',
            name='profile',
            field=models.OneToOneField(to='artisthub.UserProfile'),
        ),
        migrations.AddField(
            model_name='audioupload',
            name='album',
            field=models.ForeignKey(related_name='songs', to='artisthub.MusicAlbum'),
        ),
        migrations.AddField(
            model_name='audioupload',
            name='musician',
            field=models.ForeignKey(related_name='artists_songs', to='artisthub.Musician'),
        ),
    ]
