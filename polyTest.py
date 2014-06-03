import sfml as sf
import sys
import os
import random
import math
import utilFunctions as utlF
from utilFunctions import direction

class poly(sf.ConvexShape):
	def __init__(self,points,posX,posY,color,oColor,oThick,totMass,springConstant):
		super(poly,self).__init__()
		self.point_count=len(points)
		self.points=utlF.ccwReOrder(points)
		for i in range(self.point_count):
			self.set_point(i,(self.points[i]))

		self.position=sf.Vector2(posX,posY)
		self.posNot=self.position
		self.centroid=self.calcCentroid()
		
		self.size=sf.Vector2(utlF.calcWidth(points),utlF.calcHeight(points))
		self.topLeft=utlF.createCorners(self.position,self.size)[0]
		self.bottomRight=utlF.createCorners(self,position,self.size)[1]

		self.fill_color=color
		self.outline_color=oColor
		self.outline_thickness=oThick

		self.totMass=totMass
		self.springConstant=springConstant
		self.prevV=0
		self.goingUp=False
		self.numBounces=1
		self.curMaxHeight=posNot[1]+utlF.calcCurMaxHeight(self.springConstant,self.numBounces)
		self.deltas=[]

	def updateAll(self,pVec=None):
		if pVec==None:
			self.points=utlF.ccwReOrder(self.points)
		else:
			self.points=utlF.ccwReOrder(pVec)
		self.topLeft=utlF.createCorners(self.position,self.size)[0]
		self.bottomRight=utlF.createCorners(self.position,self.size)[1]
		self.centroid=self.calcCentroid()

	def calcCentroid(self):
		p=self.points
		p.append(p[0]) # the last point==the first point

		a=0
		c_x=0
		c_y=0

		for i in range(len(self.points)-1):
			a+=(p[i][0]*p[i+1][1]-p[i+1][0]*p[i][1])
		for i in range(len(self.points)-1):
			c_y+=(p[i][1]+p[i+1][1])*(p[i][0]*p[i+1][1]-p[i+1][0]*p[i][1])
		for i in range(len(self.points)-1):
			c_x+=(p[i][0]+p[i+1][0])*(p[i][0]*p[i+1][1]-p[i+1][0]*p[i][1])
		
		a*=(1/2)
		c_x*=(1/(6*a))
		c_y*-(1/(6*a))
		
		return sf.Vector2(c_x,c_y)

	def calcForces(self,floor,fVec=(0,0)): 
	# DO THIS AFTER: 1. refactoring bounces(springTest)
	#				 2. implementing point re-ordering
		g=98.1
		dt=1/60
		return sf.Vector2(0,0)

def main():
	window=sf.RenderWindow(sf.VideoMode(1000,600),"Poly Test")
	window.framerate_limit=60

	while window.is_open:
		window.clear(sf.Color(50,100,150,255))

		for event in window.events:
			if type(event)==sf.CloseEvent:
				#print(tSpring.deltas)
				window.close()

		window.display()




if __name__=='__main__':
	main()