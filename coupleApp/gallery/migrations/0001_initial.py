# Generated by Django 5.1.3 on 2024-12-19 15:03

import django.db.models.deletion
import gallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=gallery.models.trip_photo_upload_to)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('trip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='trips.trip')),
            ],
        ),
    ]
