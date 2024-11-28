import cv2

# Iniciar la captura de video desde la cámara
cap = cv2.VideoCapture(0)

while True:
    # Leer un frame de la cámara
    ret, frame = cap.read()
    if not ret:
        print("No se pudo acceder a la cámara.")
        break

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Aplicar detección de bordes con Canny
    canny = cv2.Canny(gray, 10, 150)
    canny = cv2.dilate(canny, None, iterations=1)
    canny = cv2.erode(canny, None, iterations=1)
    
    # Encontrar contornos
    cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        x, y, w, h = cv2.boundingRect(approx)

        # Identificar figuras según la cantidad de vértices
        if len(approx) == 3:
            cv2.putText(frame, 'Triangulo', (x, y - 5), 1, 1, (0, 255, 0), 1)

        elif len(approx) == 4:
            aspect_ratio = float(w) / h
            if aspect_ratio == 1:
                cv2.putText(frame, 'Cuadrado', (x, y - 5), 1, 1, (0, 255, 0), 1)
            else:
                cv2.putText(frame, 'Rectangulo', (x, y - 5), 1, 1, (0, 255, 0), 1)

        elif len(approx) == 5:
            cv2.putText(frame, 'Pentagono', (x, y - 5), 1, 1, (0, 255, 0), 1)

        elif len(approx) == 6:
            cv2.putText(frame, 'Hexagono', (x, y - 5), 1, 1, (0, 255, 0), 1)

        elif len(approx) > 10:
            cv2.putText(frame, 'Circulo', (x, y - 5), 1, 1, (0, 255, 0), 1)

        # Dibujar el contorno de la figura
        cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)

    # Mostrar el frame con las figuras detectadas
    cv2.imshow('Deteccion de Figuras', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()