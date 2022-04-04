import  cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(img):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def region_of_interest(img):
    
    h = img.shape[0]
    polygon = np.array([
        [(860,h),(1500,h),(1850,175)]
    ])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,polygon,255)
    masked_img = cv2.bitwise_and(img,mask)
    return masked_img
    
    
def display_lines(img,line):
    line_img = np.zeros_like(img)
    if line is not None:
        for lin in line:
            x1, y1, x2, y2 = lin.reshape(4)
            cv2.line(line_img,(x1,y1),(x2,y2),(0,0,255),10)
    return line_img
    

cap = cv2.VideoCapture("video.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    canny =  canny(frame)
    crop_img = region_of_interest(canny)
    line =cv2.HoughLinesP(crop_img,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
    line_img = display_lines(frame,line)
    combo_img = cv2.addWeighted(frame,0.8, line_img,1, 1)
    cv2.imshow("res",combo_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
   
    
   