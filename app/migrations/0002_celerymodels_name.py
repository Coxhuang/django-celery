# Generated by Django 2.0.7 on 2019-01-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='celerymodels',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
