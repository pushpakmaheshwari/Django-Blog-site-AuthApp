# Generated by Django 3.0.5 on 2020-05-19 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_upload_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='name',
            new_name='Title',
        ),
    ]
