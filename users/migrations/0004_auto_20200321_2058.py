# Generated by Django 3.0.4 on 2020-03-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofileinfo_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/user/images'),
        ),
    ]
