# Generated by Django 5.2.3 on 2025-07-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brdc', '0005_events_newsandnotice_publicationanddocuments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_adivisor',
            field=models.BooleanField(default=False),
        ),
    ]
