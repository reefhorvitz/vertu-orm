# Generated by Django 3.0.3 on 2020-03-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200320_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
