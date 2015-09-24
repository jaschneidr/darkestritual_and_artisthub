# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artisthub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.CharField(max_length=256, null=True, verbose_name=b'Facebook', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=140, verbose_name=b'Location', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.CharField(max_length=256, null=True, verbose_name=b'Twitter', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='artist_name',
            field=models.CharField(max_length=140, null=True, verbose_name=b'Artist Name', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(max_length=100000, null=True, verbose_name=b'About The Artist', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='influences',
            field=models.TextField(max_length=100000, null=True, verbose_name=b'Influences', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=140, verbose_name=b'Name', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_type',
            field=models.CharField(db_index=True, max_length=1, verbose_name=b'Artist Type', choices=[(b'A', b'Author'), (b'M', b'Musician'), (b'V', b'Visual Artist')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(max_length=140, null=True, verbose_name=b'Artist Website', blank=True),
        ),
    ]
