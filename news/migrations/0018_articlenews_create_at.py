# Generated by Django 3.1.7 on 2021-05-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_delete_galleryarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlenews',
            name='create_at',
            field=models.DateField(auto_now=True),
        ),
    ]
