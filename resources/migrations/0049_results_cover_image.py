# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-25 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('resources', '0048_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='cover_image',
            field=models.ForeignKey(blank=True, help_text='\n            Max file size: 10MB. Choose from: GIF, JPEG, PNG\n            (but pick PNG if you have the choice)\n        ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
