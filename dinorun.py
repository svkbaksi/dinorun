#!/usr/bin/python

import time
import cv2
import mss
import numpy as np
from PIL import Image
from os import system

monitor = {"top": 325, "left": 160, "width": 280, "height": 68}

with mss.mss() as sct:
	while True:
		screen = np.array(sct.grab(monitor))
		image  = cv2.cvtColor(screen, cv2.COLOR_BGRA2RGB)
		imagem = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		imagem = cv2.bitwise_not(imagem)

		signal=imagem.sum()

		print("")
		if (signal>80000) :
			time.sleep(0.2)
			system("xdotool key Up")
			print("debug info: jump")
		
		time.sleep(0.5)
