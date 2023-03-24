from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from v1 import blocks as v1_blocks
from v1.atomic_elements import organisms, schema
from v1.feeds import get_appropriate_rss_feed_url_for_page
from v1.models.learn_page import AbstractFilterPage


class BlogContent(blocks.StreamBlock):
    full_width_text = organisms.FullWidthText()
    info_unit_group = organisms.InfoUnitGroup()
    expandable = organisms.Expandable()
    well = organisms.Well()
    video_player = organisms.VideoPlayer()
    email_signup = v1_blocks.EmailSignUpChooserBlock()
    simple_chart = organisms.SimpleChart()
    faq_schema = schema.FAQ(label="FAQ schema")
    how_to_schema = schema.HowTo(label="HowTo schema", max_num=1)


class BlogPage(AbstractFilterPage):
    content = StreamField(
        BlogContent,
        use_json_field=True,
    )

    edit_handler = AbstractFilterPage.generate_edit_handler(
        content_panel=FieldPanel("content")
    )
    template = "v1/blog/blog_page.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["rss_feed"] = get_appropriate_rss_feed_url_for_page(
            self, request=request
        )

        return context


class LegacyBlogContent(BlogContent):
    content = blocks.RawHTMLBlock(
        help_text="Content from WordPress unescaped."
    )
    reusable_text = v1_blocks.ReusableTextChooserBlock("v1.ReusableText")


class LegacyBlogPage(AbstractFilterPage):
    content = StreamField(
        LegacyBlogContent,
        use_json_field=True,
    )

    edit_handler = AbstractFilterPage.generate_edit_handler(
        content_panel=FieldPanel("content")
    )
    template = "v1/blog/blog_page.html"
