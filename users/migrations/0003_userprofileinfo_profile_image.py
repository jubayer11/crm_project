# Generated by Django 3.0.4 on 2020-03-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='static/user/images'),
        ),
    ]
