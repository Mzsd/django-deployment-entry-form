from django.urls import path
from entry_form import views

# TEMPLATE TAGGING
app_name = "entry_form"

urlpatterns = [
    path('speech_recog_one', views.speech_recog, name='speech_recog_one'),
    path('speech_recog_two', views.speech_recog, name='speech_recog_two'),
    path('speech_recog_three', views.speech_recog, name='speech_recog_three'),
]