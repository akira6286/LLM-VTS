import pyttsx3

def rin_speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('voice', 'female')
    engine.say(text)
    engine.runAndWait()
