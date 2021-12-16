import cv2
import mediapipe as mp
import time

# Crio o obejto "camera"
cap = cv2.VideoCapture(0)

# Crio o objeto para verificar onde estão as minhas mãos
mpHands = mp.solutions.hands
hands = mpHands.Hands()
dotDraw = mp.solutions.drawing_utils

# frame rates dados da frame
pTime = 0  # previous Time
cTime = 0  # current Time

# Enquanto a camera estiver conectada
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks) #Mosta a posição da mao quando aparece na camera

    if results.multi_hand_landmarks:
        for Handldmk in results.multi_hand_landmarks:
            for id, lm in enumerate(Handldmk.landmark):
                h, w, c = img.shape  # altura, largura e o canal
                cx, cy = int(lm.x * w), int(lm.y * h)  # A posição estava em decima passo para numeros inteiros
                print(id, cx, cy)
                if id == 11:
                 cv2.circle(img, (cx, cy), 25, (255, 255, 5),
                               cv2.FILLED)  # desenho um circulo á volta de todos os pontos

            dotDraw.draw_landmarks(img, Handldmk, mpHands.HAND_CONNECTIONS)  # desenha

    cTime = time.time();  # frames
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, "FPS:", (4, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.99, (255, 255, 5),
                3)  # colocar na  cam a imagem dos FPS
    cv2.putText(img, str(int(fps)), (5, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.99, (255, 255, 5),
                3)  # colocar na  cam a imagem dos FPS

    cv2.imshow("IMAGEM", img)
    if cv2.waitKey(1) == ord('q'):  # O wait
        break
# ABRE A CAMERA
