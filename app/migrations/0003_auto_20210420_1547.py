# Generated by Django 3.1.6 on 2021-04-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210420_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagram',
            name='author',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='diagram',
            name='comment',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
