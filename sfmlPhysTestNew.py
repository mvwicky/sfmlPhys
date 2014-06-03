import sfmlPhys as sfPy
import sfml as sf
import sys
import os
import random
import math
import utilFunctions as utlF

def main():
	window=sfPy.scene(1000,600,"Test",sf.Color(50,100,150,255))
	
	#dArgs=utlF.getDefaultArgs(window.size.x,window.size.y)
	#window.initBox(50,50,400,300,sf.Color.MAGENTA)
	#window.initBox(50,50,500,200,sf.Color.GREEN)
	#window.initBox(50,50,600,100,sf.Color.CYAN)

	points=[(0,3),(2,0),(6,1),(7,4),(4,5),(2,6),(1,5)]
	fPoints=[(0,150),(100,0),(300,50),(350,200),(200,250),(100,300),(50,250)]
	fPoints2=[(300,50),(350,200),(200,250),(100,300),(50,250),(0,150),(100,0)]


	nPoly=sf.ConvexShape()
	nPoly.point_count=len(fPoints)
	for i in range(nPoly.point_count):
		nPoly.set_point(i,fPoints[i])


	nPoly.fill_color=sf.Color.RED
	nPoly.outline_color=sf.Color.BLACK
	nPoly.outline_thickness=1
	nPoly.origin=(0,0)
	nPoly.position=(500,300)


	while window.is_open:
		window.clear(window.color)

		for event in window.events:
			if type(event)==sf.CloseEvent:
				window.close()

		window.draw(nPoly)
		nPoly.move((-1,0))
		for i in range(nPoly.point_count):
			print(nPoly.get_point(i))

		#for i in range(len(window.objects)):
		#	window.objects[i].calcForces(window.size.y)	
		#	window.draw(window.objects[i])


		window.display()	

if __name__=='__main__':
	main()