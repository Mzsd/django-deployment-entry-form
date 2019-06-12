"""speech_recog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from entry_form import views

urlpatterns = [
    # path('speech_recog_one', views.speech_recog, name='speech_recog_one'),
    # path('speech_recog_two', views.speech_recog, name='speech_recog_two'),
    # path('speech_recog_three', views.speech_recog, name='speech_recog_three'),
    path('', views.index, name='index'),
    path('', include('entry_form.urls')),
    path('admin/', admin.site.urls),
]