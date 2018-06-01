import numpy as np
import cv2
import time


def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while cap.isOpened():
        ret, image = cap.read()

        loop_time = time.time()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.blur(gray, (3, 3))

        ret, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # detect edges in the image
        edged = cv2.Canny(thresh, 150, 255)

        # find contours (in the image
        _, contours, _ = cv2.findContours(edged.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        centers = []
        last_dimensions = []
        for contour in contours:
            # approximate the contour
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

            # if the approximated contour has four points its a rectangle
            if len(approx) == 4:
                (x, y, w, h) = cv2.boundingRect(approx)
                if h >= 40 and w >= 40:

                    aspect_ratio = w / float(h)

                    # check if the rectangle is a square
                    if 0.85 <= aspect_ratio <= 1.15:
                        print("h: " + str(h) + "  W: " + str(w))

                        moments = cv2.moments(approx)
                        m00 = moments['m00']
                        if m00 == 0:
                            m00 = 0.05

                        # get the center of the square
                        cx = int(moments['m10'] / m00)
                        cy = int(moments['m01'] / m00)
                        is_duplicate = is_a_duplicate(last_dimensions, h, w)
                        if not is_duplicate:
                            if check_if_target_found(centers, cx, cy, thresh):
                                break
                            last_dimensions.append((w, h))
                            centers.append(np.array((cx, cy)))
                            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        # print("FPS: " + str(1 / (time.time() - loop_time)))
        cv2.imshow("Image", image)
        cv2.imshow("thresh", thresh)
        # print("FPS: " + str(1/ (time.time() - loop_time)))
        str
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()


def check_if_target_found(centers, cx, cy, image) -> bool:
    first_match = True
    for center in centers:
        distance = np.linalg.norm(np.array((cx, cy)) - center)
        if distance <= 15:
            if first_match:
                first_match = False
            else:
                if is_target_in_center(cy):
                    print("ImageProcessor_target_detected")
                    cv2.drawMarker(image, (cx, cy), (0, 0, 255), markerType=cv2.MARKER_CROSS,
                                   markerSize=15, line_type=cv2.LINE_AA)
                    print(str(cx) + ' ' + str(cy))
                    return True
                else:
                    cv2.drawMarker(image, (cx, cy), (255, 0, 0), markerType=cv2.MARKER_CROSS,
                                   markerSize=15, line_type=cv2.LINE_AA)
    return False


def is_a_duplicate(last_dimensions, height, width) -> bool:
    offset = 3
    for lastDimension in last_dimensions:
        if (lastDimension[0] + offset) >= width >= (lastDimension[0] - offset):
            return True

        if (lastDimension[1] + offset) >= height >= (lastDimension[1] - offset):
            return True
    return False


def is_target_in_center(cy) -> bool:
    center_y = 480 / 2
    offset = 60
    if (center_y - offset) <= cy <= (center_y + offset):
        return True
    return False

if __name__ == '__main__':
    main()