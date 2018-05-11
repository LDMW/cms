# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-23 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('resources', '0044_auto_20180420_0423'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCollections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('heading', models.TextField(blank=True)),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('link_text', models.TextField(blank=True)),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='resources.Home')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]