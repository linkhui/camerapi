#!/usr/bin/python  
#-*- coding: utf-8 -*-  
  
import subprocess
import camera
import ftpservice
import uploadtoqiniu

def capturePicture():
    callString = 'raspistill -o image.jpg'
    subprocess.call(callString, shell = True)

#capturePicture()
filePath = camera.captureImage()
uploadtoqiniu.uploadfile(filePath)
#ftpservice.uploadfile(filePath)
