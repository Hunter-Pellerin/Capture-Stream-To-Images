import cv2, os, sys
import config

cwd = os.getcwd()
path = os.path.join(cwd, config.output_folder_name)
total_output_frames = 0

def setDir():
    if config.output_directory != "":
        path == config.output_directory
        return True
    else:
        try:
            os.chdir(path)
        except:
            os.mkdir(path)
            os.chdir(path)
        return True


def outputResizedFrames():
    total_frames = config.native_fps
    frame_index = 0 # uses the arbitrary value for desired amount of output fps
    resize_count = 0

    cap = cv2.VideoCapture("capture.avi")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        frame_index = int(total_frames / config.native_fps)
        resized = resizeImage(frame)
        cv2.imwrite(os.path.join(path, "img{}.jpg".format(frame_index)), resized)
        total_frames += config.native_fps
        cap.set(config.fps, total_frames)
        resize_count+=1
        resizeProgress(resize_count, int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    
    cap.release()
    cv2.destroyAllWindows()

def resizeImage(img):
    return cv2.resize(img, config.scaled_res, interpolation = cv2.INTER_AREA)

def resizeProgress(current_frame, total_frames):
    total_output_frames = int((total_frames / config.native_fps) * config.fps)
    progress = round((current_frame / total_output_frames * 100), 2)
    sys.stdout.write('\r')
    sys.stdout.write("Resizing: {}/{} - {}%".format(current_frame, total_output_frames, progress))
    sys.stdout.flush