'''if you are using python idle and any of the directories are installed in laptop but not importing in python idle
run the following command into you terminal. This command will run the idle with current env of your terminal.
PS do not forget to change env in which the modules are installed.
Open the terminal
Run following command
Type this on the terminal to open the IDLE with the current virtual environment
python -m idlelib
'''
'''If you are still unable to import the modules
open terminal and run the following
pip install <module_name>
Then open IDLE with current environment
'''
import urllib
import cv2
import numpy as np
import urllib.request

'''
Download IP Webcame in your phone. 
Click on the option 'start services'
Copy the IP4 address and paste it to browser.
'''
'''
Select javascript option. It will start the camera.
Right click on the image. Click on copy image url. Paste this url below on 'url' .'''

url = 'http://10.116.247.130:8080/shot.jpg'

while True:
    imgRes = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgRes.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow("test",img)
    if ord('q')==cv2.waitKey(10):
        exit(0)
