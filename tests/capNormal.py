from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FileVideoStream
from imutils.video import FPS

import numpy as np
import cv2
import imutils
import time

IMAGESIZE_X = 640
IMAGESIZE_Y =  480
TARGETRANGE = 15
TARGETOFFSET = 0


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 20)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, IMAGESIZE_X)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, IMAGESIZE_Y)

fps = FPS().start()


def getCenter(contour):
    moments = cv2.moments(contour)
    center_x = int(moments["m10"] / moments["m00"])
    center_y = int(moments["m01"] / moments["m00"])
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


while fps._numFrames < 300:
    # Capture frame-by-frame
    ret, image = cap.read()

    # Image operations
    operate = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    operate = cv2.GaussianBlur(operate, (3, 3), 0)
    # operate = cv2.blur(operate, (3, 3))
    _, operate = cv2.threshold(operate, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # find edges
    # operate = cv2.Canny(operate, 150, 255)

    # find contours
    _, contours, _ = cv2.findContours(operate.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


    #sort the contours from largest to smallest and pick the largest
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:8]

    center_array = []
    square_array = []
    for c in contours:

        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # check contour if is a rectangle
        if len(approx) == 4:
            (x, y, w, h,) = cv2.boundingRect(approx)
            if h >= 1 and w >= 1:
                ratio = w / float(h)

                # check if rectangle is a square
                if 0.85 <= ratio <= 1.15:
                    square_array.append(c)
                    cX, cY = getCenter(c)
                    center_array.append(np.array((cX, cY)))


    cX, cY = find_target(center_array)

    if not cX == -1:
        cv2.drawMarker(image, (cX, cY), (0, 255, 0), cv2.MARKER_CROSS, 15, cv2.LINE_AA)
        if checkX(cX):
            cv2.drawMarker(image, (cX, cY), (0, 0, 255), cv2.MARKER_TRIANGLE_DOWN,15, cv2.LINE_AA)




    cv2.drawContours(image, contours, -1, (255,0,0),2)
    cv2.drawContours(image, square_array, -1, (0, 255, 0), 2)




    # Display the resulting frame
    # cv2.imshow('Stasi',image)
    # cv2.imshow('oper',operate)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    fps.update()

# When everything done, release the capture
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cap.release()
cv2.destroyAllWindows()

