# Generated by Django 4.0.4 on 2022-06-11 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_group_background_group_description_group_manual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='password',
            field=models.TextField(blank=True),
        ),
    ]
