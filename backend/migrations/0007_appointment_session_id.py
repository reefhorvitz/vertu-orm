# Generated by Django 3.0.3 on 2020-03-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_property_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='session_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='opentok sessionId'),
        ),
    ]
