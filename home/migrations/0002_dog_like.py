# Generated by Django 3.0 on 2019-12-09 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
