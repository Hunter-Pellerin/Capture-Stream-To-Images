import os
from sys import stdout
from glob import glob
from time import sleep
import ftplib
import config, separateframes as sepfs

ftp = ftplib.FTP('')

sourcePath = os.path.join(os.getcwd(), config.output_folder_name)
destinationPath = config.targetDir + '/' + config.output_folder_name

def connect(ipv4, user='', passwd=''):
    ftp.connect(ipv4, 21)
    ftp.login(user, passwd)

def setTargetDir():
    ftp.cwd(config.targetDir)

def makeFolder():
    try:
        ftp.mkd(config.output_folder_name)
    except:
        pass

def gotoFolder():
    print(destinationPath)
    ftp.cwd(destinationPath)

def uploadFiles():
    counter = 1
    for img in glob(sourcePath +"/*.jpg"):
        showProgress(counter)
        filename = "img{}.jpg".format(counter)
        ftp.storbinary('STOR '+ filename, open(img, 'rb'))
        counter += 1

def showProgress(imgCount):
    stdout.write("Image {}/{}".format(imgCount, sepfs.total_output_frames))
    stdout.write('\r')
    stdout.flush()

def main():
    if config.uploadFilesToFTP == True:
        connect(config.ipv4, config.username, config.password)
        setTargetDir()
        makeFolder()
        gotoFolder()
        uploadFiles()
        ftp.quit()