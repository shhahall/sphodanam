from django.urls import path
from . import views
urlpatterns = [
    path('',views.index_page,name='index'),
    path('continue/<pk>',views.index_two,name='index2'),
    path('login/',views.login_page,name='login')
]