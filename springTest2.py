import sys
import os
import random
import math
import sfml as sf 
import utilFunctions as utlF

class spring(sf.RectangleShape):
	def __init__(self,width=None,height=None,posX=None,posY=None,color=None,
				 oColor=None,oThick=None,mass=None,k=None,dt=None):
		super(spring,self).__init__()
		
		if (width==None) or (height==None):
			self.size=(50,50)
		elif (width!=None) or (height!=None):
			self.size=(width,height)

		self.origin=(self.size[0]/2,self.size[1]/2)
		
		if (posX==None) or (posY==None):
			self.position=(0,0)
		elif (posX!=None) or (posY!=None):
			self.position=(posX,posY)

		self.topLeft=utlF.createCorners(self.position,self.size)[0]
		self.bottomRight=utlF.createCorners(self.position,self.size)[1]
		self.posNot=self.position
		self.prevV=0
		self.gravAcc=98.1

		if dt==None:
			self.dt=1/60
		elif dt!=None:
			self.dt=dt

		if color==None:
			self.fill_color=sf.Color.RED
		elif color!=None:
			self.fill_color=color
		if oColor==None:
			self.outline_color=sf.Color.BLACK
		elif oColor!=None:
			self.outline_color=oColor
		if oThick==None:
			self.outline_thickness=1
		elif oThick!=None:
			self.outline_thickness=oThick

		if mass==None:
			self.mass=10
		elif mass!=None:
			self.mass=mass

		if k==None:
			self.springConst=5
		elif k!=None:
			self.springConst=k

		self.goingUp=False
		self.deltas=[]
		self.numBounces=1
		self.curMaxHeight=self.posNot[1]+utlF.calcCurMaxHeight(self.springConst,self.numBounces)				

	def updateBounds(self):
		self.topLeft=utlF.createCorners(self.position,self.size)[0]
		self.bottomRight=utlF.createCorners(self.position,self.size)[1]

	def calcForces(self,floor,fVec=(0,0)):
	# calculates newtonian forces on the object
		self.updateBounds()
		deltaX=0
		deltaY=0

		if self.bottomRight[1]>=floor or self.goingUp==True:
		# if box is at the bottom or bouncing already
			self.goingUp=True
			self.prevV=0
			return self.bounce(floor)

		if fVec[0]!=0: # calculate deltaX
		# if there is an x force
			if self.posNot[0]==self.position[0]:
			# if the object hasn't moved
				deltaX=((self.dt**3)*fVec[0])/(2*self.mass)
			elif self.posNot[0]!=self.position[0]:
			# if the object has moved
				deltaX=((self.dt**2)*fVec[0])/self.mass

		# calculate non-bouncing deltaY
		deltaY=self.dt*(self.prevV+self.dt*((fVec[1]-(self.mass*self.gravAcc))/self.mass))

		self.prevV=deltaY*60
		self.deltas.append((deltaX,-deltaY))

		self.move(sf.Vector2(deltaX,-deltaY))

		# return non-bouncing deltas
		return sf.Vector2(deltaX,-deltaY)

	def bounce(self,floor):
	# function that calculates and moves the object in a bouncing fashion
		if self.position>=self.curMaxHeight:
		# if still in the air
			# take the new deltas from the old movement
			cDeltX=-(self.deltas[len(self.deltas)-1][0])
			cDeltY=-(self.deltas[len(self.deltas-1)][1])
			if len(self.deltas)!=1:
				del self.deltas[len(self.deltas)-1]
			self.move((cDeltX,cDeltY))
			return sf.Vector2(cDeltX,cDeltY)
		elif self.position.y<=self.curMaxHeight:
		# if on the ground
			self.goingUp=False
			self.numBounces+=1
			self.curMaxHeight+=utlF.calcCurMaxHeight(self.springConst,self.numBounces)
			self.bounceDeform(floor)

	def bounceDeform(self,floor):
	# function to make the object deform
		pass

def main():
	pass

if __name__=='__main__':
	main()