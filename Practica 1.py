import cv2
import numpy as np
import matplotlib.pyplot as plt


#Leer la imagen 
imagen = cv2.imread('colors.jpg')
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(gris, 100, 200)
#verde = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGBA)
#Muestra una imagen en una vantana
if imagen is None:
    print("No se pudo abirir e archivo")
else: 
    cv2.imshow('Imagen Originnal', imagen)
    cv2.imshow('Imagen Color', gris)
    cv2.imshow('Imagen gris bordes', bordes)
    
#Espera hasta que el ususario presione una tecla
    cv2.waitKey(0)
#Cierra todas las ventanas
    cv2.destroyAllWindows()