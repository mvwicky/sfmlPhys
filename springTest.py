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
		self.prevV=0 # velocity (deltaY) in the previous frame
		self.gravAcc=98.1 # acceleration due to gravity
		self.dt=1/60 # time per frame
		self.fill_color=color
		self.outline_color=oColor
		self.outline_thickness=oThick
		self.mass=mass
		self.springConstant=k
		self.goingUp=False
		self.deltas=[] # contains all of the deltas calculated by calcForces (don't know why)
		self.numBounces=1
		self.curMaxHeight=self.posNot[1]+(self.springConstant*((self.numBounces+3)**2)) # the max height that the spring will bounce to
		
	def updateBounds(self):
		self.topLeft=utlF.createCorners(self.position,self.size[1],self.size[0])[0]
		self.bottomRight=utlF.createCorners(self.position,self.size[1],self.size[0])[1]

	def calcForces(self,floor,fVec=(0,0)):
		self.updateBounds()

		if self.bottomRight[1]>=floor or self.goingUp==True:
			# if the box is at the bottom or already started bouncing
			#print("BOTTOM")
			self.goingUp=True
			self.prevV=0
			self.bounceDeform(floor)
			return self.bounce(floor)
		
		if self.posNot[0]==self.position.x:
			# if the box is at the initial position(force is applied for one frame only)
			deltaX=((self.dt**3)*fVec[0])/(2*self.mass)
		elif self.posNot[0]!=self.position.x:
			# if the box has movec from the inital position
			deltaX=((self.dt**2)*fVec[0])/self.mass

		deltaY=self.dt*(self.prevV+self.dt*((fVec[1]-(self.mass*self.gravAcc))/self.mass)) 
		
		self.prevV=deltaY*60
		self.deltas.append((-deltaY))

		if self.prevV!=deltaY:
			# print these if the box moved last frame
			pass
			#print("deltaY=",deltaY)
			#print("Momentum=",deltaY*self.mass)
			#print("KE=",.5*self.mass*deltaY**2)
			#print("MG=",9.81*self.mass)
			# Spring Potential Energy
			# Use it to calculate the Gravitaional Potential Energy
			# KE=

		self.move(sf.Vector2(deltaX,-deltaY))
		return sf.Vector2(deltaX,-deltaY)

	def bounce(self,floor):
		if self.position.y>=self.curMaxHeight:
		#	cDelt=-self.deltas[len(self.deltas)-1]
			cDelt=-(self.deltas[len(self.deltas)-1])
			if len(self.deltas)!=1:
				del self.deltas[len(self.deltas)-1]
			#print("cDelt=",cDelt)
			self.move((0,cDelt)) # change to iterate through deltas
			return sf.Vector2(0,cDelt)
		elif self.position.y<=self.curMaxHeight: # if apex has been reached
			self.goingUp=False
			self.numBounces+=1
			#print(self.numBounces)
			self.curMaxHeight=self.curMaxHeight+(self.springConstant*((self.numBounces+3)**2))

	def bounceDeform(self, floor, defConst=5):
		pass


def main():
	window=sf.RenderWindow(sf.VideoMode(1000,600),"Spring Test")
	window.framerate_limit=60

	tSpring=spring(50,50,500,0,sf.Color.GREEN,sf.Color.BLACK,1,10,15)

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