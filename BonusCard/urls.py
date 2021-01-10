"""BonusCard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from bonus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bonus/', views.LoyaltyListView.as_view(), name='select'),
    re_path(r'^(?P<pk>\d+)/update', views.LoyaltyUpdateView.as_view(), name='update'),
    #re_path(r'^(?P<pk>\d)+/$', views.LoyaltyDetailView.as_view(), name='card_detail'),
    re_path(r'^(?P<pk>\d+)/$', views.LoyaltyDetailView.as_view(), name='card_detail'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.LoyaltyDeleteView.as_view(), name='delete'),
    path("generator/", views.generator, name = 'card_generator'),
]

