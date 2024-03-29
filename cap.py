from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FileVideoStream
from imutils.video import FPS

import numpy as np
import cv2
import imutils
import time

IMAGESIZE_X = 640
IMAGESIZE_Y = 480
TARGETRANGE = 15
TARGETOFFSET = 20
TARGETTIMEOFFSET = 0
CENTER_ACCURANCY = 10
CENTER_MATCHES = 2
run = False


def start(reachedtargetmethod):
    global run
    run = True
    vs = WebcamVideoStream(src=0).start()
    fps = FPS().start()

    while run:
        # Capture frame-by-frame
        image = vs.read()

        # Image operations  GaussianBlur was faster then Blur, Threshold replaced Canny for faster findContours
        operate = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        operate = cv2.GaussianBlur(operate, (3, 3), 0)
        # operate = cv2.blur(operate, (3, 3))
        _, operate = cv2.threshold(operate, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # operate = cv2.adaptiveThreshold(operate,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

        # find edges
        # operate = cv2.Canny(operate, 150, 255)

        # find contours
        _, contours, _ = cv2.findContours(operate.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # sort the contours from largest to smallest and pick the largest
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:9]

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
                    if 0.9 <= ratio <= 1.1:
                        square_array.append(c)
                        cX, cY = getCenter(c)
                        center_array.append(np.array((cX, cY)))

        cX, cY = find_target(center_array)

        if not cX == -1:
            print("Target found at: " + str(cX) + "," + str(cY))
            # cv2.drawMarker(image, (cX, cY), (0, 255, 0), cv2.MARKER_CROSS, 15, cv2.LINE_AA)
            if checkX(cX):
                print("Drop location : " + str(cX) + "," + str(cY))
                # cv2.drawMarker(image, (cX, cY), (0, 0, 255), cv2.MARKER_TRIANGLE_DOWN, 15, cv2.LINE_AA)
                time.sleep(TARGETTIMEOFFSET)
                reachedtargetmethod()
                break

        # Draw the Contours
        # cv2.drawContours(image, contours, -1, (255, 0, 0), 2)
        # cv2.drawContours(image, square_array, -1, (0, 255, 0), 2)

        # Display the resulting frame
        # cv2.imshow('Stasi', image)
        # cv2.imshow('oper',operate)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        fps.update()

    # When everything done, release the capture
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    cv2.destroyAllWindows()
    vs.stop()
    # vs.stream.release()


def stop():
    global run
    run = False


def getCenter(contour):
    moments = cv2.moments(contour)
    center_x = int(moments["m10"] / moments["m00"])
    center_y = int(moments["m01"] / moments["m00"])
    return center_x, center_y


# Check the x cords and return True if the position is reached.
def checkX(x) -> bool:
    upper = IMAGESIZE_X / 2 + TARGETRANGE + TARGETOFFSET
    lower = IMAGESIZE_X / 2 - TARGETRANGE + TARGETOFFSET
    if lower <= x <= upper:
        return True
    else:
        return False


# Looking for the Target. Check the Centers of the Squares and return the Cords, if there are enough Matches.
def find_target(centers_array):
    for i, v in enumerate(centers_array[0:-2]):
        center_matches = 0
        for w in centers_array[i + 1:]:
            diff = np.abs(v - w)
            if diff[0] <= CENTER_ACCURANCY and diff[1] <= CENTER_ACCURANCY:
                center_matches += 1
                if center_matches >= CENTER_MATCHES:
                    return v[0], v[1]
    return -1, -1


if __name__ == '__main__':
    def test():
        print("Testrun Target found")


    start(test)
