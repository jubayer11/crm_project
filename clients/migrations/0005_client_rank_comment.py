# Generated by Django 3.0.4 on 2020-03-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20200322_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Rank_comment',
            field=models.CharField(blank=True, max_length=50, verbose_name='Company Ranking Comment'),
        ),
    ]
