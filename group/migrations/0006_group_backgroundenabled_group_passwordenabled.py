# Generated by Django 4.0.4 on 2022-06-16 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_message_sender_alter_message_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='backgroundEnabled',
            field=models.TextField(default='off'),
        ),
        migrations.AddField(
            model_name='group',
            name='passwordEnabled',
            field=models.TextField(default='off'),
        ),
    ]
