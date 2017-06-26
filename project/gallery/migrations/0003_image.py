# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('gallery', '0002_auto_20170626_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('image_file', filer.fields.image.FilerImageField(to='filer.Image')),
                ('obj', models.ForeignKey(to='gallery.Gallery')),
            ],
        ),
    ]
