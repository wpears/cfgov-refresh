# Generated by Django 2.2.24 on 2021-10-20 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailinventory', '0001_initial'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('v1', '0272_add_ask_search_max_length'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('paying_for_college', '0022_add_ask_search_max_length'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentLoanQuizPage',
        ),
    ]
