# Generated by Django 2.2.6 on 2020-06-16 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbltest', '0013_remove_card_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='context1',
        ),
        migrations.RemoveField(
            model_name='card',
            name='context2',
        ),
    ]
