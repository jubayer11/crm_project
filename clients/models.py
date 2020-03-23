from django.db import models

Gender = (
    ('1', 'Male'),
    ('2', 'Female'),
    ('3', 'Other')
)
English_spoken_Checking = (
    ('1', 'Yes'),
    ('2', 'No')
)
Query_received_spoken_Checking = (
    ('1', 'yes'),
    ('2', 'No')
)
Business_received_spoken_Checking = (
    ('1', 'yes'),
    ('2', 'No')
)

Company_size = (
    ('1', '2xs'),
    ('2', 'xs'),
    ('3', 's'),
    ('4', 'M'),
    ('5', 'L'),
    ('6', 'XL'),
    ('7', '2XL'),
    ('8', '3XL'),

)

Company_type = (
    ('1', 'Distributor'),
    ('2', 'Dealer'),
    ('3', 'Wholesale'),
    ('4', 'Importer'),
    ('5', 'B2b power seller '),
    ('6', 'Agent')
)

Company_ranking = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
)

Result = (('1', 'Success'), ('2', 'Claim'))


# Create your models here.

class Client(models.Model):
    client_unique_code = models.CharField(max_length=100, blank=True)

    Company_name = models.CharField(max_length=201, verbose_name='Company Name', blank=False)
    address = models.TextField(max_length=1550, blank=True, verbose_name='Address')
    City = models.CharField(max_length=200, verbose_name='City', blank=True)
    telephone = models.CharField(max_length=200, blank=True, null=True, verbose_name='Telephone No')
    contact_person_contact = models.CharField(max_length=200, blank=True, null=True, verbose_name='Telephone No')
    fax = models.CharField(max_length=200, blank=True, null=True, verbose_name='Fax No')
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name='email')
    website = models.URLField(max_length=30, blank=True, verbose_name='Website')
    Zip_code = models.IntegerField(verbose_name='Zip Code', blank=True, null=True)
    Rank = models.CharField(max_length=50, verbose_name='Company Ranking', blank=True)
    Rank_comment = models.TextField(max_length=50, verbose_name='Company Ranking Comment', blank=True)
    Communicate_date = models.DateTimeField(blank=True, null=True, verbose_name='Comunicate Date')
    Follow_up_date = models.DateTimeField(blank=True, null=True, verbose_name='Follow Up Date')
    Product_segment = models.CharField(max_length=550, blank=True, verbose_name='Product Segment')
    Products = models.CharField(max_length=550, blank=True, verbose_name='Products')
    Gender = models.CharField(blank=True, choices=Gender, max_length=20)
    Meeting_follow_up_date = models.DateTimeField(blank=True, null=True, verbose_name='Meeting Follow Up Date')
    Company_size = models.CharField(max_length=50, choices=Company_size, blank=True, verbose_name='Company Size')
    Company_type = models.CharField(max_length=500, choices=Company_type, blank=True,
                                    verbose_name='Company Type')
    Business_maturity_rate = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name='Business Maturity Rate')
    English_spoken = models.CharField(blank=True, max_length=20, choices=English_spoken_Checking, default=0,
                                      verbose_name='English Spoken')
    Query_received = models.CharField(blank=True, max_length=20, choices=Query_received_spoken_Checking, default=0,
                                      verbose_name='Query Received')
    Business_received = models.CharField(blank=True, max_length=20, choices=Business_received_spoken_Checking,
                                         default=0, verbose_name='Business Received')
    Business_result = models.CharField(blank=True, max_length=50, choices=Result, default=0,
                                       verbose_name='Business Result')
    Mode_of_payment = models.CharField(max_length=500, blank=True, verbose_name='Mode Of Payment')
    Note = models.TextField(max_length=1550, blank=True, verbose_name='Note')
    country = models.TextField(max_length=45, blank=True, verbose_name='Country')
    contact_person = models.TextField(max_length=45, blank=True, verbose_name='Contact Person')
    contact_person_designation = models.TextField(max_length=1550, blank=True,
                                                  verbose_name='Contact Person Designation')

    def __str__(self):
        return self.Company_name
