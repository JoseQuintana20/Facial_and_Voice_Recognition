import cv2
import os
import speech_recognition as sr
from moviepy.editor import *

dataPath = 'C:/Users/joseq/Documents/U/Multimedia/ProyectoFinal/ReconocimientoFacial/Data'
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
#face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo
face_recognizer.read('modeloEigenFace.xml')
#face_recognizer.read('modeloFisherFace.xml')
#face_recognizer.read('modeloLBPHFace.xml')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Jose.mp4')
#clip = VideoFileClip('Jose.mp4')

#cap = cv2.VideoCapture('Martin.mp4')
#clip = VideoFileClip('Martin.mp4')

#Extracción del adudio del video MP4
#audio = clip.audio
#audio.write_audiofile('audio.wav')

#r=sr.Recognizer()

#audio_file=sr.AudioFile('audio.wav')
#with audio_file as source:
#  audio_analizar=r.record(source)

#texto=r.recognize_google(audio_analizar,language='es-CO')


#cap = cv2.VideoCapture('Maria.mp4')
#clip = VideoFileClip('Maria.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')



while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        
        # EigenFaces
        if result[1] < 7200:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2) 
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

#print('{} dijo: {}'.format(imagePaths[result[0]], texto))
cap.release()
cv2.destroyAllWindows()