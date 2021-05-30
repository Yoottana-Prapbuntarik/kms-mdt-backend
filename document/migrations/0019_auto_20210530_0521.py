# Generated by Django 3.1.7 on 2021-05-29 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0018_documentreview_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentreview',
            name='template',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, related_name='fk_template', to='document.documenttemplate'),
        ),
    ]
