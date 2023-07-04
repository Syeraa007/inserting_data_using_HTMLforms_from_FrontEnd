"""
URL configuration for HTMLF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Forms.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form_data/',form_data,name='form_data'),
    path('form_topic/',form_topic,name='form_topic'),
    path('form_webpage/',form_webpage,name='form_webpage'),
    path('form_record/',form_record,name='form_record'),
    path('retrieve_webpage/',retrieve_webpage,name='retrieve_webpage'),
    path('webpage_result/',webpage_result,name='webpage_result'),
    path('checkbox/',checkbox,name='checkbox'),

]
