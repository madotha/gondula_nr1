from __future__ import print_function
from imutils.video import FileVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2


import numpy as np
import cv2
import imutils
import time

IMAGESIZE_X = 640
IMAGESIZE_Y =  480
TARGETRANGE = 15
TARGETOFFSET = 0


vs = FileVideoStream("test.avi").start()
time.sleep(0.5)



fps = FPS().start()


def getCenter(contour):
    moments = cv2.moments(contour)
    m00 = moments["m00"]
    if m00 == 0:
        m00 =0.01
    center_x = int(moments["m10"] / m00)
    center_y = int(moments["m01"] / m00)
    return center_x, center_y

def checkX(x) -> bool:
    upper = IMAGESIZE_X/2 + TARGETRANGE + TARGETOFFSET
    lower = IMAGESIZE_X/2 - TARGETRANGE + TARGETOFFSET
    if lower <= x <= upper:
        return True
    else:
        return False


def find_target(centers_array):
    for i, v in enumerate(centers_array[0:-2]):
        center_matches = 0
        for w in centers_array[i + 1:]:
            diff = np.abs(v - w)
            if diff[0] <= 10 and diff[1] <= 10:
                center_matches += 1
                if center_matches >= 2:
                    return v[0], v[1]
    return -1, -1

loopimage = 0
loopcontours = 0
loopforloop = 0
while vs.more():
    # Capture frame-by-frame
    image = vs.read()
    loopstart = time.time()

    # Image operations
    operate = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    operate = cv2.GaussianBlur(operate, (3, 3), 0)
    # operate = cv2.blur(operate, (3, 3))
    # _, operate = cv2.threshold(operate, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # find edges
    operate = cv2.Canny(operate, 150, 255)
    loopimage += time.time() - loopstart

    # find contours
    loopstart = time.time()
    _, contours, _ = cv2.findContours(operate.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    loopcontours += time.time() -  loopstart

    #sort the contours from largest to smallest and pick the largest
    loopstart = time.time()

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:9]
    # print(len(contours))
    center_array = []
    square_array = []
    for c in contours:

        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # check contour if is a rectangle
        if len(approx) == 4:
            (x, y, w, h,) = cv2.boundingRect(approx)
            if h >= 10 and w >= 10:
                ratio = w / float(h)

                # check if rectangle is a square
                if 0.85 <= ratio <= 1.15:
                    square_array.append(c)
                    cX, cY = getCenter(c)
                    center_array.append(np.array((cX, cY)))

    loopforloop += time.time() - loopstart
    cX, cY = find_target(center_array)

    if not cX == -1:
        # cv2.drawMarker(image, (cX, cY), (0, 255, 0), cv2.MARKER_CROSS, 15, cv2.LINE_AA)
        print("Target found at"+str(cX))
        if checkX(cX):
            print("Target Drop at" + str(cX))
            # cv2.drawMarker(image, (cX, cY), (0, 0, 255), cv2.MARKER_TRIANGLE_DOWN,15, cv2.LINE_AA)




    # cv2.drawContours(image, contours, -1, (255,0,0),2)
    # cv2.drawContours(image, square_array, -1, (0, 255, 0), 2)




    # Display the resulting frame
    # cv2.imshow('Stasi',image)
    cv2.imshow('oper',operate)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    fps.update()

# When everything done, release the capture
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print("Imagetime:"+str(loopimage))
print("Contour:"+str(loopcontours))
print("Afterloop:"+str(loopforloop))
cv2.destroyAllWindows()
vs.stop()

