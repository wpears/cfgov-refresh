from django.core.exceptions import ImproperlyConfigured
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe

from wagtail.admin.ui.tables import BooleanColumn, Column
from wagtail.images.shortcuts import get_rendition_or_not_found
from wagtail.snippets.views.snippets import SnippetViewSet

from v1.models import (
    Banner,
    Contact,
    EmailSignUp,
    PortalCategory,
    PortalTopic,
    ReusableText,
)


class BannerViewSet(SnippetViewSet):
    model = Banner
    icon = "warning"
    list_display = ["title", "url_pattern", BooleanColumn("enabled")]
    ordering = ["title"]
    search_fields = ["title", "url_pattern", "content"]
    add_to_admin_menu = True


class ContactViewSet(SnippetViewSet):
    model = Contact
    icon = "snippet"
    list_display = ["heading", "body"]
    ordering = ["heading"]
    search_fields = ["heading", "body", "contact_info"]


class EmailSignUpViewSet(SnippetViewSet):
    model = EmailSignUp
    menu_icon = "snippet"
    list_display = ["topic", "heading", "text", "code", "url"]
    ordering = ["topic"]
    search_fields = ["topic", "code", "url"]


class PortalCategoryViewSet(SnippetViewSet):
    model = PortalCategory
    menu_icon = "snippet"
    list_display = ["heading", "heading_es"]
    ordering = ["heading"]
    search_fields = ["heading", "heading_es"]


class PortalTopicViewSet(SnippetViewSet):
    model = PortalTopic
    menu_icon = "snippet"
    list_display = ["heading", "heading_es"]
    ordering = ["heading"]
    search_fields = ["heading", "heading_es"]


class ThumbnailColumn(Column):
    """Display a snippet column as an image thumbnail.

    This functionality used to exist in modeladmin but doesn't exist in
    snippets. See Wagtail guidance on migrating which recommends defining a
    custom column type:

    https://docs.wagtail.org/en/v5.2.2/reference/contrib/modeladmin/migrating_to_snippets.html#customization-of-index-view-table-rows-and-columns
    """

    def __init__(self, name, image_filter_spec, **kwargs):
        super().__init__(name, **kwargs)
        self.image_filter_spec = image_filter_spec

    def get_value(self, instance):
        try:
            image = getattr(instance, self.name)
        except AttributeError as e:
            raise ImproperlyConfigured(
                f"No attribute `{self.name}` on class `{instance.__class__.__name__}`."
            ) from e

        if not image:
            return ""

        rendition = get_rendition_or_not_found(image, self.image_filter_spec)

        img_attrs = {
            "src": rendition.url,
            "class": "admin-thumb",
            "decoding": "async",
            "loading": "lazy",
        }

        return mark_safe(f"<img{flatatt(img_attrs)}>")


class ReusableTextViewSet(SnippetViewSet):
    model = ReusableText
    menu_icon = "snippet"
    list_display = ["title", "sidefoot_heading", "text"]
    ordering = ["title"]
    search_fields = ["title", "sidefoot_heading", "text"]
