import cv2
import mediapipe as mp
import time


class detecthand():
    # inicialização
    def __init__(self, mode=False, maxhands=2, modelComplexity=1, detectionconfidence=0.5,
                 trackconfidence=0.5):  # define as variaveis vindas do main
        self.mode = mode
        self.modelComplex = modelComplexity
        self.maxhands = maxhands
        self.detectionconfidence = detectionconfidence
        self.trackconfidence = trackconfidence

        # Crio o objeto para verificar onde estão as minhas mãos

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxhands,self.modelComplex ,self.detectionconfidence, self.trackconfidence)

        self.dotDraw = mp.solutions.drawing_utils



    # encontrar a mão
    def findhand(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)  # self porque estamos a falar DESTE objeto

        if self.results.multi_hand_landmarks:
            for Handldmk in self.results.multi_hand_landmarks: #percorrer todas as mãos
                if draw:
                    self.dotDraw.draw_landmarks(img, Handldmk, self.mpHands.HAND_CONNECTIONS)  # desenha as maos
        return img



    def findPosition(self, img, handNo=0,draw=True ):

            lmList = [] #Esta será a lista de ladmarks que vamos devolver
            if self.results.multi_hand_landmarks:
                    myhand = self.results.multi_hand_landmarks[handNo] # irá fixar a primeia mão,.... e a partir dai irá definir as landmarks

                    for id, lm in enumerate(myhand.landmark):
                        h, w, c = img.shape  # altura, largura e o canal
                        cx, cy = int(lm.x * w), int(lm.y * h)  # A posição estava em decima passo para numeros inteiros

                        lmList.append([id, cx, cy])
                        #if id == 0:
                        if draw:
                             cv2.circle(img, (cx, cy), 5, (255, 255, 5),
                                       cv2.FILLED)  # desenho um circulo á volta de todos os pontos
            return lmList



def main():
    # frame rates dados da frame
    pTime = 0  # previous Time
    cTime = 0  # current Time
    cap = cv2.VideoCapture(0)  # Crio o obejto "camera"
    detector = detecthand()



    # Enquanto a camera estiver conectada
    while True:
        success, img = cap.read()

        img = detector.findhand(img)
        lmList = detector.findPosition(img)

        if len(lmList)!= 0:
            print(lmList[4]) #codigo 4 é a ponta do polegar // posso ver a localização de cada dedo

        cTime = time.time();  # frames
        cTime = time.time();  # frames
        fps = 9 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, "FPS:", (4, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.99, (255, 255, 5),
                    3)  # colocar na  cam a imagem dos FPS
        cv2.putText(img, str(int(fps)), (5, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.99, (255, 255, 5),
                    3)  # colocar na  cam a imagem dos FPS

        # ABRE A CAMERA
        cv2.imshow("PROJETO", img)
        if cv2.waitKey(1) == ord('q'):  # O wait
            break


if __name__ == "__main__":  # ou seja se o programa estiver a correr
    main()
