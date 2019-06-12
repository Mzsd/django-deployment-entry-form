import speech_recognition as sr

def get_audio():

    ACCESS_TOKEN = "HZZQJTZXSJUBKOTRQ2BPURCZACVLS7LD"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak: ")
        audio = r.listen(source)

    try:
        audio_txt = r.recognize_wit(audio, ACCESS_TOKEN)
        print(audio_txt)
        return audio_txt
    except sr.UnknownValueError:
        print("Could not understand!")
        return ""
    except sr.RequestError as e:
        print("Failed to fetch results; {0}".format(e))
        return ""

if __name__ == "__main__":
    get_audio()