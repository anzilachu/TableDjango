# Generated by Django 4.2.4 on 2023-08-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_id', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('solvent', models.CharField(max_length=100)),
                ('solvent_volume', models.CharField(max_length=100)),
                ('spike_volume', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('analysis_dilution', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Analysis',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
    ]