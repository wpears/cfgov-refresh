# -*- coding: utf-8 -*-

from django.db import migrations, models
from wagtail import fields as core_fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('applicant_type', models.CharField(max_length=255)),
                ('display_title', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['applicant_type'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='City name')),
            ],
            options={
                'ordering': ('state_id', 'name'),
            },
        ),
        migrations.CreateModel(
            name='EmailApplicationLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('address', models.EmailField(max_length=254)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=32)),
                ('salary_min', models.IntegerField()),
                ('salary_max', models.IntegerField()),
            ],
            options={
                'ordering': ['grade'],
            },
        ),
        migrations.CreateModel(
            name='GradePanel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
            ],
            options={
                'ordering': ('grade',),
            },
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_category', models.CharField(max_length=255)),
                ('blurb', core_fields.RichTextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['job_category'],
            },
        ),
        migrations.CreateModel(
            name='JobLength',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_length', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['job_length'],
            },
        ),
    ]
