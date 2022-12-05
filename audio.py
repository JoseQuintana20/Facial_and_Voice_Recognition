import threading
import time
import speech_recognition as sr
from moviepy.editor import *

r=sr.Recognizer()

audio_file=sr.AudioFile('Jose.mp4')

with audio_file as source:
  audio_analizar=r.record(source)

texto=r.recognize_google(audio_analizar,language='es-CO')

print(texto)

'''
with sr.Microphone() as recurso:
        print('Dime algo....')
        audio = r.listen(recurso)
        try:
            texto=r.recognize_google(audio,language='es-CO')
            print('Esto es lo que has dicho: {}'.format(texto))
            with open('audio.wav','wb') as fichero:
                fichero.write(audio.get_wav_data())
        except:
            print('Lo siento no te entendi')
'''
def audio_f():
    with sr.Microphone() as recurso:
        print('Dime algo....')
        audio = r.listen(recurso)
        try:
            texto=r.recognize_google(audio,language='es-CO')
            print('Esto es lo que has dicho: {}'.format(texto))
            with open('audio.wav','wb') as fichero:
                fichero.write(audio.get_wav_data())
        except:
            print('Lo siento no te entendi')
    time.sleep(10)

def worker():
    r=sr.Recognizer()
    with sr.Microphone() as recurso:
        print('Dime algo....')
        audio = r.listen(recurso)
        try:
            texto=r.recognize_google(audio,language='es-CO')
            print('Esto es lo que has dicho: {}'.format(texto))
            with open('audio.wav','wb') as fichero:
                fichero.write(audio.get_wav_data())
        except:
            print('Lo siento no te entendi')
    time.sleep(5)
    print('fin')


threads = list()
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()