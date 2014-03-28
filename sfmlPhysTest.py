debug=True

import sfmlPhys2 as sfPy 
import random
import math
if debug==True:
	import sfml as sf
	import vecFuncs as vecF

def main():
	newScene=sfPy.scene(500,500,"Phys Test",sf.Color.CYAN)
	n=0
	for i in range(10):
		newScene.initBox(50,50,25+50*i,25,sf.Color.RED,sf.Color.BLACK,1,10)
	while newScene.window.is_open:
		newScene.window.clear(newScene.color)
		for event in newScene.window.events:
			if type(event) == sf.CloseEvent:
				newScene.window.close()
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RETURN):
			newScene.window.close()
		newScene.draw(newScene.objects[0],newScene.objects[0].calcForces(newScene.windowSize[1]))
		newScene.window.display()
		newScene.resize()


if __name__ == '__main__':
	main()