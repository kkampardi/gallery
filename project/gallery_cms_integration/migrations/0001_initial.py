# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, serialize=False, related_name='gallery_cms_integration_gallerypluginmodel', parent_link=True, primary_key=True, to='cms.CMSPlugin')),
                ('gallery', models.ForeignKey(to='gallery.Gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
