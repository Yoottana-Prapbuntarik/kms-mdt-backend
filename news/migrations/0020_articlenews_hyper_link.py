# Generated by Django 3.1.7 on 2021-05-24 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_auto_20210525_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlenews',
            name='hyper_link',
            field=models.CharField(blank='', help_text='add your hyper link to readmore', max_length=255, null=True),
        ),
    ]
