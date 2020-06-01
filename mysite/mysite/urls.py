"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('authentication-login/', TemplateView.as_view(template_name='authentication-login.html'), name='authentication-login'),
    path('authentication-register/', TemplateView.as_view(template_name='authentication-register.html'), name='authentication-register'),
    path('charts/', TemplateView.as_view(template_name='charts.html'), name='charts'),
    path('pages-elements/', TemplateView.as_view(template_name='pages-elements.html'), name='pages-elements'),
    path('error-403/', TemplateView.as_view(template_name='error-403.html'), name='error-403'),
    path('error-404/', TemplateView.as_view(template_name='error-404.html'), name='error-404'),
    path('error-405/', TemplateView.as_view(template_name='error-405.html'), name='error-405'),
    path('error-500/', TemplateView.as_view(template_name='error-500.html'), name='error-500'),
    path('form-basic/', TemplateView.as_view(template_name='form-basic.html'), name='form-basic'),
    path('form-wizard/', TemplateView.as_view(template_name='form-wizard.html'), name='form-wizard'),
    path('grid/', TemplateView.as_view(template_name='grid.html'), name='grid'),
    path('icon-fontawesome/', TemplateView.as_view(template_name='icon-fontawesome.html'), name='icon-fontawesome'),
    path('icon-material/', TemplateView.as_view(template_name='icon-material.html'), name='icon-material'),
    path('index2/', TemplateView.as_view(template_name='index2.html'), name='index2'),
    path('pages-buttons/', TemplateView.as_view(template_name='pages-buttons.html'), name='pages-buttons'),
    path('pages-calendar/', TemplateView.as_view(template_name='pages-calendar.html'), name='pages-calendar'),
    path('pages-chat/', TemplateView.as_view(template_name='pages-chat.html'), name='pages-chat'),
    path('pages-gallery/', TemplateView.as_view(template_name='pages-gallery.html'), name='pages-gallery'),
    path('pages-invoice/', TemplateView.as_view(template_name='pages-invoice.html'), name='pages-invoice'),
    path('tables/', TemplateView.as_view(template_name='tables.html'), name='tables'),
    path('widgets/', TemplateView.as_view(template_name='widgets.html'), name='widgets'),
]
