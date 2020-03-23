from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Client


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'Company_name', 'City', 'Products', 'Communicate_date', 'Follow_up_date', 'Meeting_follow_up_date')
    list_filter = ('Company_name', 'Communicate_date')
    search_fields = ('Company_name', 'Note')
    list_per_page = 10
    fields = (
        ('Company_name', 'email'),
        ('City', 'address', 'country'),
        ('telephone', 'fax', 'website', 'Zip_code'),
        ('Rank', 'Company_size', 'Company_type',),
        ('Product_segment', 'Products'),
        ('Business_maturity_rate', 'Query_received', 'Business_result'),
        ('contact_person', 'contact_person_designation', 'Gender'),
        ('Communicate_date', 'Follow_up_date'),
        ('Meeting_follow_up_date', 'Mode_of_payment'),
        ('Note', 'client_unique_code')
    )


admin.site.register(Client, ClientAdmin)
