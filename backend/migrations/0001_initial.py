# Generated by Django 3.0.3 on 2020-03-20 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Property Amenity')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cooling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Property cooling data')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Property Facilities')),
            ],
        ),
        migrations.CreateModel(
            name='Heating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Property Heating data')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, verbose_name='Image url')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_one', models.CharField(max_length=200)),
                ('address_two', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.City')),
            ],
        ),
        migrations.CreateModel(
            name='OtherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Propertys Other Data')),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Property parking data')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Property Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Property Type')),
            ],
        ),
        migrations.CreateModel(
            name='UserBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(max_length=100)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.UserBase')),
                ('business_id', models.CharField(max_length=200)),
            ],
            bases=('backend.userbase',),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(verbose_name='Size in sqft')),
                ('price', models.IntegerField(verbose_name='price $/Month')),
                ('year_built', models.IntegerField(verbose_name='Year built')),
                ('bedroom_number', models.IntegerField()),
                ('bathroom_number', models.FloatField()),
                ('amenities', models.ManyToManyField(related_name='properties', to='backend.Amenity')),
                ('cooling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Cooling')),
                ('facilities', models.ManyToManyField(related_name='properties', to='backend.Facility')),
                ('heating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Heating')),
                ('images', models.ManyToManyField(related_name='properties', to='backend.Image')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Location')),
                ('other_data', models.ManyToManyField(related_name='properties', to='backend.OtherData')),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Parking')),
                ('tags', models.ManyToManyField(related_name='properties', to='backend.Tag')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Type')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Agent')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Country'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.UserBase')),
                ('tags', models.ManyToManyField(to='backend.Tag')),
            ],
            bases=('backend.userbase',),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Time of the appointment')),
                ('is_completed', models.BooleanField(verbose_name='Is the meeting happened')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Property')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_as_customer', to='backend.User')),
            ],
        ),
    ]
