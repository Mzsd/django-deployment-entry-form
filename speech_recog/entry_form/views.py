from django.shortcuts import render
from speech_recog import urls

import speech_recognition as sr
# Create your views here.

def index(request):
    return render(request, 'entry_form/index.html')

def speech_recog(request):
    sp_dict = {'sp_one': "",
               'sp_two': "",
               'sp_three': ""}

    request.get_full_path()
    audio_txt = get_audio()

    if str(request.get_full_path()) == "speech_recog_one":
        sp_dict['sp_one'] = audio_txt
    elif str(request.get_full_path()) == "speech_recog_two":
        sp_dict['sp_two'] = audio_txt
    elif str(request.get_full_path()) == "speech_recog_three":
        sp_dict['sp_three'] = audio_txt

    return render(request, 'entry_form/index.html', context=sp_dict)

def get_audio():

    ACCESS_TOKEN = "HZZQJTZXSJUBKOTRQ2BPURCZACVLS7LD"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak: ")
        audio = r.listen(source, 3, 3)

    try:
        audio_txt = r.recognize_wit(audio, ACCESS_TOKEN)
        print(audio_txt)
        return audio_txt
    except sr.UnknownValueError:
        print("Could not understand!")
        return "w"
    except sr.RequestError as e:
        print("Failed to fetch results; {0}".format(e))
        return "e"
    except Exception as e:
        print(e)
        return "end"