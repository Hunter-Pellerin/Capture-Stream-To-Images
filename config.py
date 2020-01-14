cameraID = 0 # can also use a video file

fps = 1      # unpredictable if set to anything other than 1 or 30
native_fps = 30

cap_res = (640,480)    # 480p works best
scaled_res = (224,224) # default for Jetson Nano

output_folder_name = "imgs"
output_directory = ""  # leave blank to use a new folder in the current directory


# ## ## # FTP CONFIG # ## ## #
uploadFilesToFTP = False  # uploads the converted files to an ftp server
                         # ***Requires further configuration in the uploadtoftp.py file.***

targetDir = "/home/user/documents"  #replace with your directory
ipv4 = "localhost"  # use string ex. "x.x.x.x"
username = ""       # if field left blank, assumes anonymous user
password = ""       # if field left blank assumes no password

# ## # ## # ##  ## # ## # ## #