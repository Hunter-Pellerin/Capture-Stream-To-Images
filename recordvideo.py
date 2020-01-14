import cv2, time, os
import config, displayinfo, separateframes, uploadtoftp

def setupCapture():
    cap = cv2.VideoCapture(config.cameraID)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("capture.avi", fourcc, config.native_fps, config.cap_res)
    frameCounter=1

    while cap.isOpened:
        ret, currentFrame = cap.read()
        if ret == True:
            out.write(currentFrame)
            frameCounter += 1
            totalImages = int((frameCounter / config.native_fps) * config.fps)
            displayinfo.drawTextOnFeed(currentFrame, "Frames: {}".format(str(totalImages)), (15,30), (0,0,0))
            cv2.imshow("OpenCV Image Processor", currentFrame)
            if checkKeyPress():
                break
        else:
            break
    destroyCapture(cap, out)

def checkKeyPress():
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True
    else:
        return False

def destroyCapture(capture, output):
    capture.release()
    output.release()
    cv2.destroyAllWindows()

def cleanUpDir():
    os.remove("capture.avi")

if __name__ == "__main__":
    separateframes.setDir()
    setupCapture()
    separateframes.outputResizedFrames()
    time.sleep(0.5) # ensure avi file is finalized
    cleanUpDir()
    time.sleep(2)
    uploadtoftp.main()