# Generated by Django 2.2.5 on 2020-01-26 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0002_auto_20200126_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectallocation',
            old_name='subjects',
            new_name='subject',
        ),
    ]
