# %%Import the necessary libraries for image processing

#.1 the numeric Standard-Library numpy
import numpy as np

#.2 Opencv
import cv2

#Matplotlib
import matplotlib.pyplot as plt

# %% Load the provided test image using OpenCV
test_img = cv2.imread("C:/Users/DELL/Desktop/Bildanalysis/Image_for_test.jpeg")
if test_img is None :
    raise FileNotFoundError( "Bild Nicht gefunden")  


#.1 Find the image size
width = test_img.shape[1]
heigth = test_img.shape[0]

#.2 create teh output image (optional)
cv2.namedWindow("Ausgabebild",cv2.WINDOW_NORMAL)
#.3 Scaling the Window to the image size
cv2.resizeWindow("Ausgabebild",width,heigth)
#.4 Displaz the image using OpenCV
cv2.imshow("Ausgebebild",test_img)
#.5 Image stands and waits for a touch from the keyboard
cv2.waitKey(0)
#.6 Tidy up all the pictures
cv2.destroyAllWindows() 

# %% Display the provided image using Matplotlib
plt.imshow(test_img)
plt.show()

# %% Fix the issue you observed by using convert-color-function
convert_test_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2RGB)
plt.imshow(convert_test_img)
plt.show()

# %%
