# Generated by Django 4.1.7 on 2023-03-27 19:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_position_category_position_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Position',
            new_name='Location',
        ),
        migrations.RenameField(
            model_name='url',
            old_name='position_url',
            new_name='location_url',
        ),
    ]
