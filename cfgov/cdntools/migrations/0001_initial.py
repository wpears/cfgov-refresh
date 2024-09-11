# Generated by Django 4.2.14 on 2024-08-20 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # This model moved from v1. We'll reuse that existing table.
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='CDNHistory',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('created', models.DateTimeField(auto_now_add=True)),
                        ('subject', models.CharField(max_length=2083)),
                        ('message', models.CharField(max_length=255)),
                        ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                    ],
                    options={
                        'db_table': 'v1_cdnhistory',
                    },
                ),
            ],
            database_operations=[],
        )
    ]
