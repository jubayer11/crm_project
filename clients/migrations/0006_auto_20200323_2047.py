# Generated by Django 3.0.4 on 2020-03-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_client_rank_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Rank_comment',
            field=models.TextField(blank=True, max_length=50, verbose_name='Company Ranking Comment'),
        ),
    ]