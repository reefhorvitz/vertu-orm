# Generated by Django 3.0.3 on 2020-03-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200320_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbase',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]