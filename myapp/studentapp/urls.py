from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('indexlogic',views.indexlogic,name='indexlogic')
   
]