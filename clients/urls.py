from django.urls import path, include

from . import views

app_name = 'clients'
urlpatterns = [

    # client information
    path('create-client', views.createClient, name='createClient'),
    path('all-client', views.allClient.as_view(), name='allClient'),
    path('submit-client', views.submitClient, name='submitClient'),
    path('delete-client/<code>', views.deletClient, name='deleteClient'),

]
