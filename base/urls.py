from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name=''),
    path('register/' , views.register , name='register'),
    path('loginPage/' , views.loginPage , name='loginPage'),
    path('LogOUTuser/' , views.LogOUTuser , name='LogOUTuser'),

    path('dashBoard/' , views.dashBoard , name='dashBoard'),
    path('create/' , views.create , name='create'),
    path('updateClient/<int:pk>' , views.updateClient , name='updateClient'),
    path('viewClient/<int:pk>' , views.viewClient , name='viewClient'),
    path('delete/<int:pk>' , views.delete , name='delete'),
]