# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-05-08 05:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0055_remove_homesitemap_link_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TopResources',
            new_name='ResourceCollections',
        ),
    ]