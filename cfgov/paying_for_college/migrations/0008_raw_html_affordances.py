# Generated by Django 3.2.24 on 2024-03-05 19:48

from django.db import migrations
import v1.blocks
import wagtail.blocks
import wagtail.contrib.typed_table_block.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('paying_for_college', '0007_add_table_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegecostspage',
            name='content',
            field=wagtail.fields.StreamField([('full_width_text', wagtail.blocks.StreamBlock([('content', wagtail.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.blocks.StructBlock([('content_block', wagtail.blocks.RichTextBlock()), ('anchor_link', wagtail.blocks.StructBlock([('link_id', wagtail.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False))]))])), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('image_width', wagtail.blocks.ChoiceBlock(choices=[('full', 'Full width'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))])), ('table', wagtail.blocks.StructBlock([('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('text_introduction', wagtail.blocks.CharBlock(required=False)), ('options', wagtail.blocks.MultipleChoiceBlock(choices=[('is_full_width', 'Display the table at full width'), ('stack_on_mobile', 'Stack the table columns on mobile')], required=False)), ('data', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.blocks.CharBlock()), ('numeric', wagtail.blocks.FloatBlock()), ('rich_text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link', 'superscript']))]))])), ('quote', wagtail.blocks.StructBlock([('body', wagtail.blocks.TextBlock()), ('citation', wagtail.blocks.TextBlock(required=False))])), ('cta', wagtail.blocks.StructBlock([('slug_text', wagtail.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('is_link_boldface', wagtail.blocks.BooleanBlock(default=False, required=False))]))])), ('related_links', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('paragraph', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('is_link_boldface', wagtail.blocks.BooleanBlock(default=False, required=False))])))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', v1.blocks.EmailSignUpChooserBlock()), ('well', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(label='Well', required=False))]))])), ('info_unit_group', wagtail.blocks.StructBlock([('format', wagtail.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('intro', wagtail.blocks.RichTextBlock(required=False)), ('link_image_and_heading', wagtail.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('border_radius_image', wagtail.blocks.ChoiceBlock(choices=[('none', 'None'), ('rounded', 'Rounded corners'), ('circle', 'Circle')], help_text='Adds a <em>border-radius</em> class to images in this group, allowing for a rounded or circular border.', label='Border radius for images?', required=False)), ('info_units', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], default={'level': 'h3'}, required=False)), ('body', wagtail.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('is_link_boldface', wagtail.blocks.BooleanBlock(default=False, required=False))]), required=False))]), default=[]))])), ('expandable_group', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Added as an <code>&lt;h3&gt;</code> at the top of this block. Also adds a wrapping <code>&lt;div&gt;</code> whose <code>id</code> attribute comes from a slugified version of this heading, creating an anchor that can be used when linking to this part of the page.', required=False)), ('body', wagtail.blocks.RichTextBlock(required=False)), ('is_accordion', wagtail.blocks.BooleanBlock(required=False)), ('has_top_rule_line', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of expandable group.', required=False)), ('is_faq', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to add FAQ schema markup to expandables.', label='Uses FAQ schema', required=False)), ('expandables', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(required=False)), ('icon', wagtail.blocks.CharBlock(required=False)), ('is_bordered', wagtail.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.blocks.BooleanBlock(required=False)), ('is_larger_heading', wagtail.blocks.BooleanBlock(required=False)), ('is_expanded_padding', wagtail.blocks.BooleanBlock(required=False)), ('content', wagtail.blocks.StreamBlock([('paragraph', wagtail.blocks.RichTextBlock(required=False)), ('well', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(label='Well', required=False))])), ('links', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('is_link_boldface', wagtail.blocks.BooleanBlock(default=False, required=False))])), ('info_unit_group', wagtail.blocks.StructBlock([('format', wagtail.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('intro', wagtail.blocks.RichTextBlock(required=False)), ('link_image_and_heading', wagtail.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('border_radius_image', wagtail.blocks.ChoiceBlock(choices=[('none', 'None'), ('rounded', 'Rounded corners'), ('circle', 'Circle')], help_text='Adds a <em>border-radius</em> class to images in this group, allowing for a rounded or circular border.', label='Border radius for images?', required=False)), ('info_units', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], default={'level': 'h3'}, required=False)), ('body', wagtail.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('is_link_boldface', wagtail.blocks.BooleanBlock(default=False, required=False))]), required=False))]), default=[]))]))], blank=True))])))])), ('expandable', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(required=False)), ('icon', wagtail.blocks.CharBlock(required=False)), ('is_bordered', wagtail.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.blocks.BooleanBlock(required=False)), ('is_larger_heading', wagtail.blocks.BooleanBlock(required=False)), ('is_expanded_padding', wagtail.blocks.BooleanBlock(required=False)), ('content', wagtail.blocks.StreamBlock([('paragraph', wagtail.blocks.RichTextBlock(required=False)), ('well', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(label='Well', required=False))])), ('links', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('is_link_boldface', wagtail.blocks.BooleanBlock(default=False, required=False))])), ('info_unit_group', wagtail.blocks.StructBlock([('format', wagtail.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('intro', wagtail.blocks.RichTextBlock(required=False)), ('link_image_and_heading', wagtail.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('border_radius_image', wagtail.blocks.ChoiceBlock(choices=[('none', 'None'), ('rounded', 'Rounded corners'), ('circle', 'Circle')], help_text='Adds a <em>border-radius</em> class to images in this group, allowing for a rounded or circular border.', label='Border radius for images?', required=False)), ('info_units', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], default={'level': 'h3'}, required=False)), ('body', wagtail.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('is_link_boldface', wagtail.blocks.BooleanBlock(default=False, required=False))]), required=False))]), default=[]))]))], blank=True))])), ('well', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(label='Well', required=False))])), ('raw_html_block', wagtail.blocks.RawHTMLBlock(label='Raw HTML block'))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='collegecostspage',
            name='header',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='For guidelines on creating heroes, visit our <a href="https://cfpb.github.io/design-system/patterns/heroes">Design System</a>. Character counts (including spaces) at largest breakpoint:<ul class="help">    <li>&bull; 41 characters max (one-line heading)</li>    <li>&bull; 82 characters max (two-line heading)</li></ul>', required=False)), ('heading_continued', wagtail.blocks.CharBlock(help_text='Use if the heading needs to break to a second lineat a specific point in the text.', required=False)), ('body', wagtail.blocks.RichTextBlock(help_text='Character counts (including spaces) at largest breakpoint:<ul class="help">    <li>&bull; 165-186 characters (after a one-line heading)</li>    <li>&bull; 108-124 characters (after a two-line heading)</li></ul>', label='Sub-heading', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='When saving illustrations, use a transparent background. ', label='Large image', required=False)), ('small_image', wagtail.images.blocks.ImageChooserBlock(help_text='<b>Optional.</b> Provides an alternate image for small displays when using a photo or bleeding hero. Not required for the standard illustration. ', required=False)), ('background_color', wagtail.blocks.CharBlock(help_text='Specify a hex value (including the # sign) from our <a href="https://cfpb.github.io/design-system/foundation/color">official color palette</a>.', required=False)), ('is_white_text', wagtail.blocks.BooleanBlock(help_text='<b>Optional.</b> Turns the hero text white. Useful if using a dark background color or background image.', label='White text', required=False)), ('is_overlay', wagtail.blocks.BooleanBlock(help_text='<b>Optional.</b> Uses the large image as a background under the entire hero, creating the "Photo" style of hero (see <a href="https://cfpb.github.io/design-system/patterns/heroes">Design System</a> for details). When using this option, make sure to specify a background color (above) for the left/right margins that appear when screens are wider than 1200px and for the text section when the photo and text stack at mobile sizes.', label='Photo', required=False)), ('is_bleeding', wagtail.blocks.BooleanBlock(help_text='<b>Optional.</b> Select if you want the illustration to bleed vertically off the top and bottom of the hero space.', label='Bleed', required=False))])), ('text_introduction', wagtail.blocks.StructBlock([('eyebrow', wagtail.blocks.CharBlock(help_text='Optional: Adds an H5 eyebrow above H1 heading text. Only use in conjunction with heading.', label='Pre-heading', required=False)), ('heading', wagtail.blocks.CharBlock(required=False)), ('intro', wagtail.blocks.RichTextBlock(required=False)), ('body', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('is_link_boldface', wagtail.blocks.BooleanBlock(default=False, required=False))]), required=False)), ('has_rule', wagtail.blocks.BooleanBlock(help_text='Check this to add a horizontal rule line to bottom of text introduction.', label='Has bottom rule', required=False))])), ('featured_content', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.TextBlock(help_text='Line breaks will be ignored.')), ('post', wagtail.blocks.PageChooserBlock(required=False)), ('show_post_link', wagtail.blocks.BooleanBlock(label='Render post link?', required=False)), ('post_link_text', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('is_link_boldface', wagtail.blocks.BooleanBlock(default=False, required=False))]), label='Additional Links')), ('video', wagtail.blocks.StructBlock([('video_id', wagtail.blocks.RegexBlock(error_messages={'invalid': 'The YouTube video ID is in the wrong format.'}, help_text='Enter the YouTube video ID, which is located at the end of the video URL, after "v=". For example, the video ID for https://www.youtube.com/watch?v=1V0Ax9OIc84 is 1V0Ax9OIc84.', label='YouTube video ID', regex='^[\\w-]{11}$', required=False)), ('thumbnail_image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional thumbnail image to show before and after the video plays. If the thumbnail image is not set here, the video player will default to showing the thumbnail that was set in (or automatically chosen by) YouTube.', required=False))], required=False))]))], blank=True, use_json_field=True),
        ),
    ]
