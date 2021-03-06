from django.urls import path, include

from . import views

app_name = 'user'
urlpatterns = [
    path('dashboard2', views.dashboard2, name='dashboard-2'),

    # users information
    path('', views.dashboard2, name='dashboard-2'),
    path('myAccount/<username>', views.myAccount.as_view(), name='myAccount'),
    path('create-users', views.createUser.as_view(), name='createUser'),
    path('all-users', views.allUser.as_view(), name='allUser'),
    path('roles', views.allRole.as_view(), name='allRole'),
    path('submit-user', views.submitUser, name='submitUser'),
    path('edit-user/<username>', views.editUser, name='editUser'),
    path('submit-edit-user/<username>', views.submitEditUser, name='submitEditUser'),
    path('delete-user/<username>', views.deletUser, name='deleteUser'),
    path('calendar', include('schedule.urls')),
    path('view-user/<username>', views.viewUser, name='viewUser'),

    ##role
    path('delete-role/<roleName>', views.deleteRole, name='deleteRole'),
    path('edit-role/<roleName>', views.editRole, name='editRole'),
    path('create-roles', views.createRole.as_view(), name='createRole'),
    path('submit-role', views.submitRole, name='submitRole'),

]
