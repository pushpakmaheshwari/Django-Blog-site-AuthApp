# Generated by Django 3.0.5 on 2020-05-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='Description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
