from django.urls import path
from . import views

urlpatterns=[
    path('result/<sub>',views.result,name='result'),
    path('add/',views.add_one,name='addone'),
    path('addcomplete/<sem>',views.add_two,name='addtwo'),
]