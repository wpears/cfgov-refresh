# Generated by Django 4.2.14 on 2024-08-20 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0035_add_footnotes'),
    ]

    operations = [
        # This model is moving to cdntools.
        # We'll reuse the existing table.
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='CDNHistory',
                ),
            ],
            database_operations=[],
        )
    ]
