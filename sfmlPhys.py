import sfml as sf
import sys
import os
import random
import math
import vecFuncs as vecF
import utilFunctions as utlF

class poly(sf.ConvexShape):
	def __init__(self, points,posX,posY,color,oColor,oThick,totMass):
		self.point_count=len(points)
		self.points=self.ccwReOrder(points)
		self.position=(posX,posY)
		self.topLeft=sf.Vector2()
		self.bottomRight=sf.Vector2()
		self.fill_color=color
		self.outline_color=oColor
		self.outline_thickness=oThick
		self.calcCentroid()
		self.totMass=totMass
	def updateAll(self):
		self.calcCentroid()
		self.ccwReOrder(self.points)
	def ccwReOrder(self,pVec):
		for i in range(len(pVec)):
			pass
	def calcCentroid(self):
		self.ccwReOrder(self.points)
		a=float(0)
		c_x=float(0)
		c_y=float(0)
		for i in range(len(self.points)-1):
			a+=float(self.points[i][0]*self.points[i+1][1]-self.points[i+1][0]*self.points[i][1]) 
		for i in range(len(self.points)-1):
			c_y+=float((self.points[i][1]+self.points[i+1][1])*(self.points[i][0]*self.points[i+1][1]-self.points[i+1][0]*self.points[i][1]))
		for i in range(len(self.points)-1):
			c_x+=float((self.points[i][0]+self.points[i+1][0])*(self.points[i][0]*self.points[i+1][1]-self.points[i+1][0]*self.points[i][1]))
		a*=(float(1)/float(2))		
		c_x*=(1/(6*a))
		c_y*=(1/(6*a))
		self.centroid=sf.Vector2(c_x,c_y)
		return sf.Vector2(c_x,c_y)

class box(sf.RectangleShape):
	def __init__(self,width,height,posX,posY,color,oColor,oThick,mass):
		super(box, self).__init__()
		self.origin=(width/2,height/2)
		self.size=(width,height)
		self.position=(posX,posY)
		self.topLeft=utlF.createCorners(self.position,self.size[1],self.size[0])[0]
		self.bottomRight=utlF.createCorners(self.position,self.size[1],self.size[0])[1]
		self.xnot=self.position.x # initial position
		self.prevV=0
		self.fill_color=color
		self.outline_color=oColor
		self.outline_thickness=oThick
		self.mass=mass
	def updateBounds(self):
		self.topLeft=utlF.createCorners(self.position,self.size[1],self.size[0])[0]
		self.bottomRight=utlF.createCorners(self.position,self.size[1],self.size[0])[1]
	def calcForces(self,floor,fVec=(0,0)):
		self.updateBounds()
		if self.bottomRight[1]>=floor:
			return sf.Vector2(0,0)
		g=98.1
		dt=1/60
		if self.xnot==self.position.x:
			deltaX=((dt**3)*fVec[0])/(2*self.mass)
		elif self.xnot!=self.position.x:
			deltaX=((dt**2)*fVec[0])/self.mass
		deltaY=dt*(self.prevV+dt*((fVec[1]-(self.mass*g))/self.mass))
		self.prevV=deltaY*60
		return sf.Vector2(deltaX,-deltaY)


class circle(sf.CircleShape):
	def __init__(self,radius,posX,posY,color,oColor,oThick,mass):
		super(circle,self).__init__()
		self.radius=radius
		self.origin=(radius,radius)
		self.position=(posX,posY)
		self.topLeft=utlF.createCorners(self.position,radius,radius)[0]
		self.bottomRight=utlF.createCorners(self.position,radius,radius)[1]
		self.xnot=self.position.x
		self.prevV=0
		self.fill_color=color
		self.outline_color=oColor
		self.outline_thickness=oThick
		self.mass=mass
	def updateBounds(self):
		self.topLeft=utlF.createCorners(self.position,self.size[1],self.size[0])[0]
		self.bottomRight=utlF.createCorners(self.position,self.size[1],self.size[0])[1]
	def calcForces(self,floor,fVec=(0,0)):
		self.updateBounds()
		if self.bottomRight[1]>=floor:
			return sf.Vector2(0,0)
		g=98.1
		dt=1/60
		if self.xnot==self.position.x:
			deltaX=((dt**3)*fVec[0])/(2*self.mass)
		elif self.xnot!=self.position.x:
			deltaX=((dt**2)*fVec[0])/self.mass
		deltaY=dt*(self.prevV+dt*((fVec[1]-(self.mass*g))/self.mass))
		self.prevV=deltaY*60
		return sf.Vector2(deltaX,-deltaY)

class line(sf.RectangleShape): # implementation is iffy
	def __init__(self,sPoint,ePoint):
		super(line,self).__init__()
		self.endPoints=[list(sPoint),list(ePoint)]
		self.length=utlF.calcLength(sPoint,ePoints)
		self.slope=utlF.calcSlope(sPoint,ePoint)
		self.angle=utlf.calcAngleDeg(sPoint,ePoint)
		self.pAngle=0
		self.size=(self.length,2)
		self.origin=(0,1)
		self.fill_color=sf.Color.BLACK
		self.outline_color=sf.Color.BLACK
		self.outline_thickness=0
		self.postion=sPoint
		self.rotate(self.angle-self.pAngle)
	def updateAll(self,sPoint,ePoint):
		self.position=sPoint
		self.endPoints=[list(sPoint),list(ePoint)]
		self.length=utlF.calcLength(sPoint,ePoint)
		self.slope=utlF.calcSlope(sPoint,ePoint)
		self.pAngle=self.angle
		self.angle=utlF.calcAngleDeg(sPoint,ePoint)
		self.rotate(self.angle-self.pAngle)


	

class scene(sf.RenderWindow):
	def __init__(self,windowWidth,windowHeight,title,color,icon=None):
		super(scene,self).__init__(self,sf.VideoMode(windowWidth,windowHeight),title)
		self.framerate_limit=60
		self.color=color
		if icon != None:
			self.icon=icon.pixels
		self.objects=[]
	def initPoly(self):
		pass
	def initBox(self):
		pass
	def initCircle(self):
		pass
	def initLine(self):
		pass	
	def draw(self):
		pass

def main():
	pass

if __name__=='__main__':
	main()