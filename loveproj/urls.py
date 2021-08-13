"""loveproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from loveapp.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('account/', include('account.urls')),
    path('loveapp_1/', include('loveapp_1.urls')),
    path('loveapp_2/', include('loveapp_2.urls')),
    path('loveapp_3/', include('loveapp_3.urls')),
    path('loveapp_4/', include('loveapp_4.urls')),
    path('loveapp_5/', include('loveapp_5.urls')),
    path('loveapp_6/', include('loveapp_6.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

