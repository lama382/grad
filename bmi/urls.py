from django.urls import path,include
#from .views import  exp
from . import views


urlpatterns = [
path('home/',views.home, name='home') ,
 path('accounts/', include('allauth.urls')),


]
