from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from .models import Client, Company_size, Company_type, Gender, Company_ranking


class myAccount(TemplateView):
    template_name = 'dashboard/profile/myAccount.html'


class allClient(TemplateView):
    template_name = 'dashboard/client/allClient.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context


def createClient(request):
    company_size = Company_size
    company_type = Company_type
    gender = Gender
    args = {'company_size': company_size, 'company_type': company_type, 'gender': gender,
            'Company_ranking': Company_ranking}
    return render(request, "dashboard/client/createClient.html", args)


def submitClient(request):
    if request.method == 'POST':
        uniqueCode = request.POST["uniqueCode"]
        clientName = request.POST["clientName"]
        clientContactName = request.POST["clientContactName"]
        clientContactDesignation = request.POST["clientContactDesignation"]
        gender = request.POST["gender"]
        contactNumber = request.POST["contactNumber"]
        email = request.POST["email"]
        website = request.POST['website']
        fax = request.POST['fax']
        telephone = request.POST['telephone']
        address = request.POST['address']
        city = request.POST['city']
        zip_code = request.POST['zip_code']
        country = request.POST['country']
        products = request.POST['products']
        productsSagement = request.POST['productsSagement']
        business_maturity_rate = request.POST['business_maturity_rate']
        business_ranking = request.POST['business_ranking']
        mode_of_payment = request.POST['mode_of_payment']
        company_size = request.POST['company_size']
        company_type = request.POST['company_type']
        Note = request.POST['Note']
        follow_up_date_time = request.POST['follow_up_date_time']
        client = Client(client_unique_code=uniqueCode, Company_name=clientName,
                        Meeting_follow_up_date=follow_up_date_time, contact_person=clientContactName,
                        contact_person_designation=clientContactDesignation, Gender=gender,
                        contact_person_contact=contactNumber, email=email, website=website, fax=fax,
                        telephone=telephone, address=address, City=city, Zip_code=zip_code, country=country,
                        Products=products,
                        Product_segment=productsSagement, Business_maturity_rate=business_maturity_rate,
                        Rank=business_ranking, Mode_of_payment=mode_of_payment, Company_size=company_size,
                        Company_type=company_type, Note=Note)
        client.save()
        return redirect('clients:allClient')


def deletClient(request, code):
    client = Client.objects.get(client_unique_code=code)
    client.delete()
    return redirect('clients:allClient')
