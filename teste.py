import pyautogui as p
import cv2
import math
import mediapipe as mp

mp_hands = mp.solutions.hands #captura o contorno da mao

mp_drawin = mp.solutions.drawing_utils #Desenha o contorno

#iniciando o Midia Pipe
hand = mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)

#captura a imagem 

cap = cv2.VideoCapture(0)


#obtendo o tamanho de tela
screen_width,screen_heigth = p.size()

#funcao para calcular a distancia entre os dois pontos 

def calcucalate_distance(p1,p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

while True:
    ret, frame = cap.read()
    if not ret:
        break
     # Obtendo as dimensões do frame
    frame_height, frame_width, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hand.process(frame_rgb)

    frame_height, frame_width, _ = frame.shape
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            #extraindo as coordenadas do ponto 8 (dedo indicador) e do ponto 4 (polegar)
            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            distance = calcucalate_distance(index_finger_tip, thumb_tip)
            x = int(index_finger_tip.x * frame_width)
            y = int(index_finger_tip.y * frame_width)

            screen_x = screen_width - (screen_width / frame_width * x)
            screen_y = screen_width - (screen_width / frame_width * y)

            if distance < 0.05:
                p.click()
                mp_drawin.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Tracking da mão",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#liberação dos Recursos
cap.release()
cv2.destroyAllWindows()

