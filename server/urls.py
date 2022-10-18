"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.challenge4, name='challenge4')
Class-based views
    1. Add an import:  from other_app.views import challenge4
    2. Add a URL to urlpatterns:  path('', challenge4.as_view(), name='challenge4')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from challenge4 import urls
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenge4/', include('challenge4.urls'), name='challenge4'),
    path('register/', user_views.register, name='register')
]
