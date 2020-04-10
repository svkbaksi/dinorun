import time
import cv2
import mss
import numpy as np
from os import system

monitor = {"top": 335, "left": 130, "width": 150, "height": 45}

print("Let's play dinorun .... ");

with mss.mss() as sct:
	while True:
		screen = np.array(sct.grab(monitor))
		image  = cv2.bitwise_not(cv2.cvtColor(screen, cv2.COLOR_BGRA2GRAY))
		signal = image.sum()
		
		if (signal>80000) :
			time.sleep(0.11)
			system("xdotool key Up")
