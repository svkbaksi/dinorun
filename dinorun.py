import time
import cv2
import mss
import numpy as np
from os import system

object_mon = {"top": 335, "left": 189, "width": 200, "height": 80}

with mss.mss() as sct:
	while True:
		image = cv2.cvtColor(np.array(sct.grab(object_mon)), cv2.COLOR_BGRA2GRAY)
		
		if ( image.sum() > 250000 ) :
			image = cv2.bitwise_not(image)
					
		if ( image.sum() > 70000 ) :
			time.sleep(0.1)
			system("xdotool key Up")
