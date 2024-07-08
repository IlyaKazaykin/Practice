"""
URL configuration for mydjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stock_exchange import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('company/', views.CompanyListAPIView.as_view(), name='company-list'),
    path('company/create/', views.CompanyCreateAPIView.as_view(), name='company-create'),
    path('buyer/', views.BuyerListAPIView.as_view(), name='buyer-list'),
    path('buyer/create/', views.BuyerCreateAPIView.as_view(), name='buyer-create'),
    path('deal/', views.DealListAPIView.as_view(), name='deal-list'),
    path('deal/create/', views.DealCreateAPIView.as_view(), name='deal-create'),
]