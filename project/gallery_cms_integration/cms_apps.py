from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url


from gallery.views import IndexView

class GalleryApphook(CMSApp):
    app_name = "gallery"
    name = _("Gallery Application")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["gallery.urls"]

    """ Instead of defining the URL patterns in another file return the directly"""
    def get_urls(self, page=None, language=None, **kwargs):
        return [
            url(r'^$', IndexView.as_view()),
            # url(r'^(?P<slug>[\w-]+)/?$', GalleryDetailView.as_view()),
        ]

apphook_pool.register(GalleryApphook)  # register the application