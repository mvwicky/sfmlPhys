import sfmlPhys as sfPy
import sfml as sf
import sys
import os
import random
import math
import utilFunctions as utlF

def main():
	window=sfPy.scene(1000,600,"Test",sf.Color(50,100,150,255))

	dArgs=utlF.getDefaultArgs(window.size.x,window.size.y)

	window.initBox(50,50,400,300,sf.Color.MAGENTA)
	window.initBox(50,50,500,200,sf.Color.GREEN)
	window.initBox(50,50,600,100,sf.Color.CYAN)

	while window.is_open:
		window.clear(window.color)

		for event in window.events:
			if type(event)==sf.CloseEvent:
				window.close()

		for i in range(len(window.objects)):
			window.objects[i].calcForces(window.size.y)
			window.draw(window.objects[i])


		window.display()	

if __name__=='__main__':
	main()