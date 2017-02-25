import time
import picamera

def captureVideo():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        camera.start_recording('foo.h264')
        camera.wait_recording(60)
        camera.stop_recording()
        camera.stop_preview()

def captureImage():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        hourminute = time.strftime("%H%M", time.localtime()) 
        fileName = 'image-'+hourminute+'.jpg'
        imageFile = '/home/pi/web/www/captureimages/'+fileName
        print(imageFile)
        camera.capture(imageFile)
        return imageFile

if __name__ == '__main__':
    captureImage()
