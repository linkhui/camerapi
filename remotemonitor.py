#!/usr/bin/python  
#-*- coding: utf-8 -*-  
  
import subprocess
import camera
import ftpservice

def capturePicture():
    callString = 'raspistill -o image.jpg'
    subprocess.call(callString, shell = True)

#capturePicture()
filePath = camera.captureImage()
ftpservice.uploadfile(filePath)
