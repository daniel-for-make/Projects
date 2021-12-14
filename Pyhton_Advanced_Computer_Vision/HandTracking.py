import cv2
import mediapipe as mp
import time

#Crio o obejto "camera"
cap = cv2.VideoCapture(0)

#Crio o objeto para verificar onde estão as minhas mãos
mpHands = mp.solutions.hands
hands = mpHands.Hands()


#Enquanto a camera estiver conectada
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    cv2.imshow("IMAGEM", img)
    if cv2.waitKey(1) == ord('q'): #O wait
        break
#ABRE A CAMERA
