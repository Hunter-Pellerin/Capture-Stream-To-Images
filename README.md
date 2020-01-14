# Capture-Stream-To-Images
Uses OpenCV (currently using the python wrapper, may also use C++ soon) to process a video feed from a webcam and output each frame as an image. The FPS and resolutions are easily customizable, along with many other options available in the config.py document.


# Prerequisites:
-Python (tested using 3.8.1 x64)

-OpenCV (tested using 4.1.2)

-Webcam (tested using Logitech C270)


# Instructions:
1. Input desired settings in config.py

2. Run the "recordvideo.py" file in terminal.

3. Recording starts immediately after the capture
   window is opened.

4. Press 'q' on the keyboard to quit at any time.

5. Images will be saved in a subfolder within the
   current working directory after quitting.

6. Change settings for ftp upload if desired (not required).


# What these scripts do:

- Start video capture (set capture resolution, default 480p)

- Live indicator of how many frames will be converted to images (set output fps vs native fps)

- Output to video file for frame conversion (video file automatically deleted)

- Resize all output images to a desired resolution

- Write images to a new folder (default in the current working directory)

- Upload to ftp server if desired (credentials required before program execution)


# Note:
This software is in very early development and is not currently designed for any professional or mission-critical
usage. Please look elsewhere for those needs.
