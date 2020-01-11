import cv2
import os
import sys

import config

cwd = os.getcwd()
path = os.path.join(cwd, config.output_folder_name)

def setDir():
    try:
        os.chdir(path)
    except:
        os.mkdir(path)
        os.chdir(path)

def getFrames():
    totalFrames = config.native_fps
    frameIndex = 0 # uses the arbitrary value for desired amount of output fps
    resizeCount = 0

    cap = cv2.VideoCapture("capture.avi")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        frameIndex = int(totalFrames / config.native_fps)
        resized = resizeImage(frame)
        cv2.imwrite(os.path.join(path, "img{}.jpg".format(frameIndex)), resized)
        totalFrames += config.native_fps
        cap.set(config.fps, totalFrames)
        resizeCount+=1
        resizeProgress(resizeCount, int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    
    cap.release()
    cv2.destroyAllWindows()

def resizeImage(img):
    return cv2.resize(img, config.scaled_res, interpolation = cv2.INTER_AREA)

def resizeProgress(currentFrame, totalFrames):
    totalOutputFrames = int(totalFrames * (config.fps/config.native_fps))
    progress = round((currentFrame / totalOutputFrames * 100), 2)
    sys.stdout.write('\r')
    sys.stdout.write("{}/{} - {}%".format(currentFrame, totalOutputFrames, progress))
    sys.stdout.flush