# Generated by Django 4.0.4 on 2022-06-11 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='background',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='group',
            name='manual',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='group',
            name='private',
            field=models.TextField(blank=True),
        ),
    ]
