# Generated by Django 3.2.20 on 2023-08-09 09:06

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_music_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='image_file',
            field=models.FileField(null=True, upload_to=core.models.music_image_file_path),
        ),
    ]
