from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError

from .models import CustomUser, UserProfileInfo


class dashboard2(TemplateView):

    def get_template_names(self):
        template_name = "dashboard-2.html"
        return template_name


class myAccount(TemplateView):
    template_name = 'dashboard/profile/myAccount.html'


class allUser(TemplateView):
    template_name = 'dashboard/users/allUser.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CustomUser.objects.all()
        return context


class createUser(TemplateView):
    template_name = 'dashboard/users/create_user.html'


def editUser(request, username):
    user = CustomUser.objects.get(username=username)
    args = {'user': user}
    return render(request, "dashboard/users/edit_user.html", args)


def submitUser(request):
    if request.method == 'POST':
        userName = request.POST["userName"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]
        designation = request.POST['designation']

        user = CustomUser(username=userName,
                          email=email,
                          first_name=firstName,
                          last_name=lastName,
                          password=make_password(password))
        user.save()

        userInfo = UserProfileInfo(user=user,
                                   designation=designation)
        userInfo.save()

    return redirect('user:allUser')


def submitEditUser(request, username):
    if username:
        user = CustomUser.objects.get(username=username)
        if request.method == 'POST':
            userName = request.POST["userName"]
            firstName = request.POST["firstName"]
            lastName = request.POST["lastName"]
            email = request.POST["email"]
            password = request.POST["password"]
            designation = request.POST['designation']
            phoneNo = request.POST['phoneNo']
            user.first_name = firstName
            user.last_name = lastName
            user.email = email
            user.password = make_password(password)
            user.username = userName
            user.save()
            userInfo = UserProfileInfo.objects.get(user=user)
            userInfo.user = user
            userInfo.designation = designation
            userInfo.phone_no = phoneNo
            try:
                displayImage = request.FILES['displayImage']
                userInfo.profile_image = displayImage
                userInfo.save()
            except MultiValueDictKeyError:
                userInfo.save()

    return redirect('user:allUser')


def deletUser(request, username):
    user = CustomUser.objects.get(username=username)
    user.delete()
    return redirect('user:allUser')

