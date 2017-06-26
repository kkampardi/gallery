# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slice', models.SlugField(unique=True)),
                ('featured_image', filer.fields.image.FilerImageField(to='filer.Image', related_name='featured')),
            ],
        ),
    ]
