# Generated by Django 2.2.5 on 2020-01-28 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0003_auto_20200126_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='academic_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='academic_term', to='DB.AcademicYear'),
        ),
    ]
