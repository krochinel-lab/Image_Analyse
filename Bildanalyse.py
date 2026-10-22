# %%Die Bibiotheken importieren

#.1 die numerische Standard-Bibiothek
import numpy as np
#.2 Opencv
import cv2
#Matplotlib
import matplotlib.pyplot as plt

# %% Lade das Bild mit Opencv
test_img = cv2.imread("C:/Users/DELL/Desktop/Bildanalysis/TestImage.png")
if test_img is None :
    raise FileNotFoundError( "Bild Nicht gefunden")  


#.1 Die Bildgröße finden
width = test_img.shape[1]
heigth = test_img.shape[0]

#.2 Ausgabebild anlegen (optional)
cv2.namedWindow("Ausgabebild",cv2.WINDOW_NORMAL)
#.3 Skalierung des Fenster auf die Bildgröße
cv2.resizeWindow("Ausgabebild",width,heigth)
#.4 Das Bild mit Opencv zeigen
cv2.imshow("Ausgebebild",test_img)
#.5 Stehende Zeit für Das Bild und Warte auf Tastatur
cv2.waitKey(0)
#.6 Alle Bilder aufräumen
cv2.destroyAllWindow() 

# %%
