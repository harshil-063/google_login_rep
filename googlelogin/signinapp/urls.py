from . import views
from django.urls import path,include
from  allauth.account.views import LogoutView
urlpatterns = [
    path('', views.signin),
    path('profile/',views.profile),
    
]
