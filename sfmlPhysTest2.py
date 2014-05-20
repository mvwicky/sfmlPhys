debug=True

import sfmlPhysOld as sfPy 
import random
import math
if debug==True:
	import sfml as sf
	import vecFuncs as vecF


def clicked():
	if sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
		while (sf.Mouse.is_button_pressed(sf.Mouse.LEFT)):
			if not sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
				return True
	return False

def main():
	newScene=sfPy.scene(500,500,"Phys Test",sf.Color.CYAN)
	
	while newScene.window.is_open:
		newScene.window.clear(newScene.color)

		newScene.initBox(50,50,50,50,sf.Color.RED,sf.Color.BLACK,1,10)
		newScene.initBox(50,50,150,50,sf.Color.YELLOW,sf.Color.BLACK,1,10)

		for event in newScene.window.events:
			if type(event) == sf.CloseEvent:
				newScene.window.close()
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RETURN):
			newScene.window.close()

		#for i in range(len(newScene.objects)):
		for i in range(2):
			newScene.draw(newScene.objects[i], newScene.objects[i].calcForces(500,(0,0)))


		#print(sf.Mouse.get_position(newScene.window))
		newScene.window.display()


if __name__=='__main__':
	main()
