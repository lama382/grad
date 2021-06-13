from django.urls import path
#from .views import  exp
from . import views
urlpatterns = [
path('exp/',views.exp, name='exp') ,
path('upload/',views.upload, name='upload') ,
path('list/',views.book_list, name='book_list') ,
path('uploadbook/',views.upload_book, name='upload_book') ,



]
