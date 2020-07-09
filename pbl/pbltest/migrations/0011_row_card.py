# Generated by Django 2.2.5 on 2020-07-08 14:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200623_0924'),
        ('pbltest', '0010_testcard_base_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='row_Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('context', models.TextField(blank=True)),
                ('context1', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.User')),
                ('cover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pbltest.UPCard')),
            ],
            options={
                'verbose_name_plural': 'row_Card',
            },
        ),
    ]
