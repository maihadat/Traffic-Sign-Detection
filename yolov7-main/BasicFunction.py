import cv2
#import imutils
import os
import time


def detect(source, weight='best.pt', conf_thres="0.5"):
    s = time.time()
    command = "python detect.py --weights " + weight + " --conf " +\
              conf_thres + " --img-size 640 --source " + source +\
              " --save-txt " + "--update"
    os.system(command)
    with open('runs/detect/rs.txt', 'r') as rs:
        lines = rs.readlines()
        lines = [line.rstrip().split(' ') for line in lines]
        lines = [[float(idx) for idx in line] for line in lines]
    open('runs/detect/rs.txt', 'w').close()
    e = time.time()
    return lines, e-s


if __name__=='__main__':
    print(detect("inference/images/bus.jpg"))

'''
id = 0
#id = 'rtsp://admin:L2E03F0A@192.168.39.232:80/cam/realmonitor?channel=1&subtype=0&unicast=false&proto=Onvif'
cap = cv2.VideoCapture(id)
rotate = 0

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#writer= cv2.VideoWriter('basicvideo(2).avi', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

while True:
    success,frame = cap.read()
    if success:
        if rotate != 0:
            frame = imutils.rotate(frame, rotate)

        #writer.write(frame)
        cv2.imshow('webcam',frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('d'):
        rotate += -90
    if key == ord('a'):
        rotate += 90

cap.release()
writer.release()
cv2.destroyAllWindows()
'''