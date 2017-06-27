from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from gallery_cms_integration.models import GalleryPluginModel
from django.utils.translation import ugettext as _


class GalleryPluginPublisher(CMSPluginBase):
    model = GalleryPluginModel  # model where plugin data are saved
    module = _("Gallery")
    name = _("Gallery Plugin")  # name of the plugin in the interface
    render_template = "gallery_cms_integration/gallery_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(GalleryPluginPublisher)  # register the plugin