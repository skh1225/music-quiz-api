# Generated by Django 3.2.20 on 2023-08-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20230804_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
    ]
