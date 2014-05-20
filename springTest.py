import sfml as sf
import sys
import os
import random
import math
import vecFuncs as vecF
import utilFunctions as utlF

class spring(sf.RectangleShape):
	def __init__(self,width,height,posX,posY,color,oColor,oThick,mass,k=5):
		super(spring,self).__init__()
		self.origin=(width/2,height/2)
		self.size=(width,height)
		self.position=(posX,posY)
		self.topLeft=utlF.createCorners(self.position,self.size[1],self.size[0])[0]
		self.bottomRight=utlF.createCorners(self.position,self.size[1],self.size[0])[1]
		self.posNot=self.position # initial position
		self.prevV=0
		self.fill_color=color
		self.outline_color=oColor
		self.outline_thickness=oThick
		self.mass=mass
		self.springConstant=k**2
		self.goingUp=False
		self.deltas=[] # contains all of the deltas calculated by calcForces (don't know why)
		self.curMaxHeight=self.posNot[1]-k # the max height that the spring will bounce to
	def updateBounds(self):
		self.topLeft=utlF.createCorners(self.position,self.size[1],self.size[0])[0]
		self.bottomRight=utlF.createCorners(self.position,self.size[1],self.size[0])[1]
	def calcForces(self,floor,fVec=(0,0)):
		self.updateBounds()
		if self.bottomRight[1]>=floor or self.goingUp==True:
			print("BOTTOM")
			self.goingUp=True
			self.prevV=0
			self.bounce(floor)
		g=98.1
		dt=1/60
		if self.posNot[0]==self.position.x:
			deltaX=((dt**3)*fVec[0])/(2*self.mass)
		elif self.posNot[0]!=self.position.x:
			deltaX=((dt**2)*fVec[0])/self.mass
		deltaY=dt*(self.prevV+dt*((fVec[1]-(self.mass*g))/self.mass))
		self.prevV=deltaY*60
		self.deltas.append((-deltaY))
		self.move(sf.Vector2(deltaX,-deltaY))
		if self.prevV!=deltaY:
			print("deltaY=",deltaY)
			print("Momentum=",deltaY*self.mass)
			print("KE=",.5*self.mass*deltaY**2)
			print("MG=",9.81*self.mass)
			# Spring Potential Energy
			# Use it to calculate the Gravitaional Potential Energy
			# KE=
		return sf.Vector2(deltaX,-deltaY)
	def bounce(self,floor):
		if self.position.y>=self.curMaxHeight:
			cDelt=-self.deltas[len(self.deltas)-1]
			del self.deltas[len(self.deltas)-1]
			print("cDelt=",cDelt)
			self.move((0,cDelt)) # change to iterate through deltas
		elif self.position.y<=self.curMaxHeight:
			self.goingUp=False
			self.curMaxHeight=self.curMaxHeight+self.springConstant


def main():
	window=sf.RenderWindow(sf.VideoMode(1000,600),"Spring Test")
	window.framerate_limit=60

	tSpring=spring(50,50,500,300,sf.Color.GREEN,sf.Color.BLACK,1,10)

	while window.is_open:
		window.clear(sf.Color(50,100,150,255))

		tSpring.calcForces(600)

		for event in window.events:
			if type(event)==sf.CloseEvent:
				#print(tSpring.deltas)
				window.close()


		window.draw(tSpring)

		window.display()


if __name__=='__main__':
	main()