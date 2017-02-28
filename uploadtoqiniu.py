# -*- coding: utf-8 -*-
 
import time
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os

import ConfigParser

access_key = '' #这里的密钥填上刚才我让你记住的密钥对
secret_key = '' #这里的密钥填上刚才我让你记住的密钥对

def readconf():
    cf = ConfigParser.ConfigParser()
    cf.read("camerapi.conf")
    global access_key,secret_key
    access_key = cf.get("qiniu", "accesskey")
    secret_key = cf.get("qiniu", "secretkey")

def uploadfile(localFilePath):
    #需要填写你的 Access Key 和 Secret Key
    #access_key = '1_NOKO0I8dW3pe1hgF4vfe5TTwroyYZG-rqIbSe_' #这里的密钥填上刚才我让你记住的密钥对
    #secret_key = '7nqJUN4zsd40CtUqndVY-ZLhiP16HMCnSQuLJxaq' #这里的密钥填上刚才我让你记住的密钥对
 
    readconf()
    print access_key,secret_key

    #构建鉴权对象
    q = Auth(access_key, secret_key)
   
    #要上传的空间
    bucket_name = 'mypi'
    
    #上传到七牛后保存的文件名
    #key = '%s_%s_%s_%s_%s_%s.jpg'%(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4],time.localtime()[5])
    remoteFileName = os.path.basename(localFilePath)#'image.jpg'

     #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, remoteFileName, 3600)
      
      #要上传文件的本地路径
    #localfile = '/home/pi/web/www/captureimages/image-1810.jpg'
       
    ret, info = put_file(token, remoteFileName, localFilePath)
        
if __name__ == '__main__':
    uploadfile("image.jpg")
