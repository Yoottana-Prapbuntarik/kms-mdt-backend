# Generated by Django 3.1.7 on 2021-05-24 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemodel',
            old_name='img',
            new_name='image',
        ),
    ]
