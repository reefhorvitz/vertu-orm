# Generated by Django 3.0.3 on 2020-03-20 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200320_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Image'),
        ),
    ]
