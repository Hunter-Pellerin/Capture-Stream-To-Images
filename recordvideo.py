import cv2, time, os
import config, displayinfo, separateframes

def setupCapture():
    cap = cv2.VideoCapture(config.cameraID)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("capture.avi", fourcc, config.native_fps, config.cap_res)

    while cap.isOpened:
        ret, current_frame = cap.read()
        if ret == True:
            out.write(current_frame)
            # total_images = (out.get(cv2.CAP_PROP_FRAME_COUNT) / config.native_fps) * config.fps
            # displayinfo.drawTextOnFeed(current_frame, str(int(total_images)), (20,20), (255,0,0))
            cv2.imshow("OpenCV Image Processor", current_frame)
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
    separateframes.getFrames()
    time.sleep(0.5) # ensure avi file is finalized
    cleanUpDir()