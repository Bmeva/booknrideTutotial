# Generated by Django 5.0.6 on 2024-06-30 16:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='Userfolder/profile_pictures')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='Userfolder/cover_photos')),
                ('DOB', models.DateTimeField()),
                ('address_line1', models.CharField(max_length=200)),
                ('adress_line2', models.CharField(max_length=200)),
                ('nationality', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_or_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_number', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
