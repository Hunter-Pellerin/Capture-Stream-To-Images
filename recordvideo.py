import cv2
from time import sleep
import os

import separateframes
import config

def checkKeyPress():
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True
    else:
        return False

def setupCapture():
    cap = cv2.VideoCapture(config.cameraID)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("capture.avi", fourcc, config.native_fps, config.cap_res)

    while cap.isOpened:
        ret, currentFrame = cap.read()
        if ret == True:
            out.write(currentFrame)
            cv2.imshow("OpenCV Image Processor", currentFrame)
            if checkKeyPress():
                break
        else:
            break
    destroyCapture(cap, out)

def destroyCapture(capture, output):
    capture.release()
    output.release()
    cv2.destroyAllWindows()

def cleanUpDir():
    os.remove("capture.avi")

if __name__ == "__main__":
    separateframes.setDir()
    setupCapture()
    separateframes.getFrames()
    sleep(0.5) # ensure avi file is finalized
    cleanUpDir()