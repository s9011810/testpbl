# Generated by Django 2.2.5 on 2020-07-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbltest', '0002_auto_20200705_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_img', models.CharField(max_length=5000)),
            ],
        ),
    ]