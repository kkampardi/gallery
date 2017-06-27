from django.db import models
from cms.models import CMSPlugin
from gallery.models import Gallery


class GalleryPluginModel(CMSPlugin):
    gallery = models.ForeignKey(Gallery)

    def __str__(self):
        return self.gallery.title
