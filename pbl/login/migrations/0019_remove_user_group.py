# Generated by Django 2.2.5 on 2020-07-28 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_user_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='group',
        ),
    ]
