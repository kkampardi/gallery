from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from gallery.models import Gallery


class GalleryToolbar(CMSToolbar):
    supported_apps = (
        'gallery',
        'gallery_cms_integration',
    )

    watch_models = [Gallery]

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('gallery-app', _('Gallery'))

        menu.add_sideframe_item(
            name=_('Gallery list'),
            url=admin_reverse('gallery_gallery_changelist'),
        )

        menu.add_modal_item(
            name=_('Add new gallery'),
            url=admin_reverse('gallery_gallery_add'),
        )


toolbar_pool.register(GalleryToolbar)  # register the toolbar
