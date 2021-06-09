from django.contrib import admin
from django.urls import path
from sqliteapp.views import cutomer, show_customer
from sqliteapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cutomer, name='customer'),
    path('ac/', views.show_customer, name='show'),
]
