# Generated by Django 2.2.4 on 2020-09-01 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_user_class_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='class_a',
        ),
    ]
