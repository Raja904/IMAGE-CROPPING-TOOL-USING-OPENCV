import cv2
import numpy as np

img = cv2.imread("images/dog.jpeg")
flag = False
xi = -1
yi = -1 

def crop(event,x,y,flags,params):
    
    global flag ,xi,yi
    flag = False
    temp_img = img.copy()
    if event == 1:
        flag = True
        xi = x
        yi = y

    elif event == cv2.EVENT_MOUSEMOVE and flag:
        cv2.rectangle(temp_img, pt1=(xi, yi), pt2=(x, y), thickness=1, color=(0, 0, 0))
        cv2.imshow("window", temp_img)

    elif event == 4:
        flag = False
        cv2.rectangle(img,pt1 = (xi,yi), pt2 =(x,y), thickness = 1,color=(0,0,0))
        img2 = img[xi-10:x+10,yi-10:y+10]
        cv2.imshow("window1",img2)
        
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",crop)


while True:
    
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x') :
        break

cv2.destroyAllWindows()




    


    

