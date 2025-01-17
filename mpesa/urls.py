

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('index/', views.index , name='index'),
    path('payment/', views.payment , name='payment'),
    path('success/', views.success , name='success'),
    path('base/', views.base , name='base'),
    

]