debug=True

import sfmlPhys2 as sfPy 
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
#	for i in range(10):
#		newScene.initBox(50,50,25+50*i,25,sf.Color.RED,sf.Color.BLACK,1,10)
	coords=[]
	while newScene.window.is_open:
		newScene.window.clear(newScene.color)
		newScene.initCircle(10,sf.Mouse.get_position(newScene.window).x,sf.Mouse.get_position(newScene.window).y,sf.Color.YELLOW,sf.Color.BLACK,1,10)
		newScene.draw(newScene.objects[0])
		for event in newScene.window.events:
			if type(event) == sf.CloseEvent:
				newScene.window.close()
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RETURN):
			newScene.window.close()
		if (clicked()):
			coords.append(sf.Mouse.get_position(newScene.window))
		print coords
		newScene.window.display()
		newScene.objects[0].setPos(sf.Mouse.get_position(newScene.window))


if __name__=='__main__':
	main()
