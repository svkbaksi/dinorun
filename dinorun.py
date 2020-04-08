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
		sct_img = sct.grab(monitor)

		img = Image.new("RGB", sct_img.size)
		pixels = zip(sct_img.raw[2::4], sct_img.raw[1::4], sct_img.raw[0::4])
		img.putdata(list(pixels))
		output = "sct-dino.png".format(**monitor)
		mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
		image = cv2.imread(output)

		imagem = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		imagem = cv2.bitwise_not(imagem)

		signal=imagem.sum()

		print("")
		if (signal>80000) :
			time.sleep(0.2)
			system("xdotool key Up")
			print("debug info: jump")
		
		time.sleep(0.5)
