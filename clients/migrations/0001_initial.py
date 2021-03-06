# Generated by Django 3.0.4 on 2020-03-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=201, verbose_name='Company Name')),
                ('address', models.TextField(blank=True, max_length=1550, verbose_name='Address')),
                ('City', models.CharField(blank=True, max_length=200, verbose_name='City')),
                ('telephone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Telephone No')),
                ('fax', models.CharField(blank=True, max_length=200, null=True, verbose_name='Fax No')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('website', models.URLField(blank=True, max_length=30, verbose_name='Website')),
                ('Post_code', models.IntegerField(blank=True, null=True, verbose_name='Zip Code')),
                ('Rank', models.CharField(blank=True, max_length=50, verbose_name='Company Ranking')),
                ('Communicate_date', models.DateTimeField(blank=True, null=True, verbose_name='Comunicate Date')),
                ('Follow_up_date', models.DateTimeField(blank=True, null=True, verbose_name='Follow Up Date')),
                ('Product_segment', models.CharField(blank=True, max_length=550, verbose_name='Product Segment')),
                ('Products', models.CharField(blank=True, max_length=550, verbose_name='Products')),
                ('Gender', models.CharField(blank=True, choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], max_length=20)),
                ('Meeting_follow_up_date', models.DateTimeField(blank=True, null=True, verbose_name='Meeting Follow Up Date')),
                ('Company_size', models.CharField(blank=True, choices=[('1', '2xs'), ('2', 'xs'), ('3', 's'), ('4', 'M'), ('5', 'L'), ('6', 'XL'), ('7', '2XL'), ('8', '3XL')], max_length=50, verbose_name='Company Size')),
                ('Company_type', models.CharField(blank=True, choices=[('1', 'Distributor'), ('2', 'Dealer'), ('3', 'Wholesale'), ('4', 'Importer'), ('5', 'B2b power seller '), ('6', 'Agent')], max_length=500, verbose_name='Company Type')),
                ('Business_maturity_rate', models.IntegerField(blank=True, null=True, verbose_name='Business Maturity Rate')),
                ('English_spoken', models.CharField(blank=True, choices=[('1', 'Yes'), ('2', 'No')], default=0, max_length=20, verbose_name='English Spoken')),
                ('Query_received', models.CharField(blank=True, choices=[('1', 'yes'), ('2', 'No')], default=0, max_length=20, verbose_name='Query Received')),
                ('Business_received', models.CharField(blank=True, choices=[('1', 'yes'), ('2', 'No')], default=0, max_length=20, verbose_name='Business Received')),
                ('Business_result', models.CharField(blank=True, choices=[('1', 'Success'), ('2', 'Claim')], default=0, max_length=50, verbose_name='Business Result')),
                ('Mode_of_payment', models.CharField(blank=True, max_length=500, verbose_name='Mode Of Payment')),
                ('Note', models.TextField(blank=True, max_length=1550, verbose_name='Note')),
                ('country', models.TextField(blank=True, max_length=45, verbose_name='Country')),
                ('contact_person', models.TextField(blank=True, max_length=45, verbose_name='Contact Person')),
                ('contact_person_designation', models.TextField(blank=True, max_length=1550, verbose_name='Contact Person Designation')),
            ],
        ),
    ]
