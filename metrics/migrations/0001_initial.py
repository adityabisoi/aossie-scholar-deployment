# Generated by Django 2.2.3 on 2020-07-23 06:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarName', models.CharField(max_length=40)),
                ('scholarImage', models.URLField()),
                ('workplace', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pubCount', models.CharField(max_length=100, null=True)),
                ('citCount', models.CharField(max_length=100, null=True)),
                ('hIndex', models.CharField(max_length=100, null=True)),
                ('gIndex', models.CharField(max_length=100, null=True)),
                ('mIndex', models.CharField(max_length=100, null=True)),
                ('oIndex', models.CharField(max_length=100, null=True)),
                ('eIndex', models.CharField(max_length=100, null=True)),
                ('hMedian', models.CharField(max_length=100, null=True)),
                ('TNCc', models.CharField(max_length=100, null=True)),
                ('sIndex', models.CharField(max_length=100, null=True)),
                ('titles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), size=None)),
                ('nCitations', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None)),
                ('citations', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None)),
                ('coauthors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None)),
                ('years', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None)),
            ],
        ),
    ]
