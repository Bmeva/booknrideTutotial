# Generated by Django 5.0.6 on 2024-07-14 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_userprofile_cover_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='Userfolder/profile_pictures'),
        ),
    ]
