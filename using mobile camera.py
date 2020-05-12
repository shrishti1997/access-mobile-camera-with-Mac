import urllib
import cv2
import numpy as np
import urllib.request
url = 'http://10.116.247.130:8080/shot.jpg'

while True:
    imgRes = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgRes.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow("test",img)
    if ord('q')==cv2.waitKey(10):
        exit(0)
