# Generated by Django 2.1.7 on 2019-03-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0003_auto_20190305_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
