import datetime
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')# microsoft sound api
voices = engine.getProperty('voices')
engine.setProperty('voic',voices[0].id)

def speak(audio):
    ''' in this jarvis will be able to speak '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    # name = input("enter your name : ")
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak('Good Morning')
    elif hour>=12 and hour< 18 :
        speak('good Afternoon')
    else:
        speak('Good evening')
    speak( f" hello I am a jaarvis. shubham create me to help you")


def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print(audio)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio ,language='en-us')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query
if __name__ == "__main__":
    wishMe()
    takeCommand()


# import speech_recognition as sr

# r=sr.Recognizer()
# # print(sr.Microphone.list_microphone_names())
# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source,duration=1)
#     # r.energy_threshold()
#     print("say anything : ")
#     audio= r.listen(source)
#     r.pause_threshold = 1
#     try:
#         text = r.recognize_google(audio)
#         print(text)
#     except:
#         print("sorry, could not recognise")


