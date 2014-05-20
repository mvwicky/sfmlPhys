import sfml as sf
import sys
import os
import random
import math
import vecFuncs as vecF

class physObject(object): # contains a bounding box
	def __init__(self,size=(50,50),topLeft=(0,0),bottomRight=(50,50),mass=10):
		self.size=size
		self.topLeft=topLeft
		self.bottomRight=bottomRight
		self.center=sf.Vector2((topLeft[0]+(size[0]/2)),(topLeft[1]+(size[1]/2)))
		self.prevV=0
		self.xnot=self.center.x
		self.mass=mass
	def inVPlane(self, xCoord):
		if (xCoord >= self.topLeft[0] and xCoord <= self.bottomRight[0]):
			return True
		else:
			return False
	def inHPlane(self, yCoord):
		if (yCoord >= self.topLeft[1] and yCoord <= self.bottomRight[1]):
			return True	
		else:
			return False
	def inObj(self, pVec):
		if (vecTest(pVec)):
			if (self.inVPlane(pVec[0]) and self.inHPlane(pVec[1])):
				return True
			else:
				return False
		elif not vecTest(pVec):
			return False
	def calcForces(self,floor,fVec=(0,0)):
		if self.bottomRight[1]>=floor:
			return sf.Vector2(0,0)
		g=98.1
		dt=1/60
		deltaX=0
		deltaY=0
		if self.xnot==self.center.x: # at the beginning
			deltaX=((dt**3)*fVec[0])/(2*self.mass)
		elif self.xnot!=self.center.x: # moved
			deltaX=((dt**2)*fVec[0])/self.mass
		deltaY = dt * (self.prevV + dt * ((fVec[1] - (self.mass * g)) / self.mass))
		self.prevV=float(deltaY)*float(60)
		return sf.Vector2(deltaX,-deltaY)

class poly(object): # at some point maybe make it inherit physObject. At this
					# point it'll be too hard cause of the possible angled bottoms
					# and uneven weight distribution
	def __init__(self,points,posX,posY,color,oColor,oThick,totMass):
		self.type="poly"
		self.poly=sf.ConvexShape()
		self.points=points
		self.points.append(points[0])
		self.poly.point_count=len(points)
		# set points
		self.poly.position=(posX,posY)
		self.poly.fill_color=color
		self.poly.outline_color=oColor
		self.poly.outline_thickness=oThick
		self.totMass=totMass
		self.centroid=sf.Vector2()
		self.topRight=sf.Vector2()
		self.bottomLeft=sf.Vector2()
	# functions 
	def calcCentroid(self): # calculates the centroid of the polygon
		self.reOrderPoints()
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
	def updateAll(self):
		self.calcCentroid()
	def reOrderPoints(self): # orders 
		for i in range(self.poly.point_count):
			pass
 
def line(object): # class to visually represent lines
	def __init__(self,lPoint,rPoint):
		self.type="line"
		self.dLine=sf.RectangleShape() # the drawn component of the line
		self.endPoints=[list(lPoint),list(rPoint)] # end points of the line
		#self.length=
		#self.slope=
		self.line.size(self.length,2)
		self.line.origin(self.length/2, 1)
		line.fill_color=sf.Color.BLACK
		line.outline_color=sf.Color.BLACK
		# set position
	def setPos(self,pVec): # 
		self.dLine.position=pVec
		# recalculate the end points
	def move(self,pVec):
		self.dLine.move(pVec)
		# recalculate end points
	def rotate(self, theta): # rotate around the origin
		self.dLine.rotate(theta)
		# recalculate the end points


class box(physObject):
	def __init__(self, width=50,height=50,posX=0,posY=0,color=sf.Color.RED,
				 oColor=sf.Color.BLACK,oThick=1,mass=10):
		super(box, self).__init__(size=(width,height),topLeft=(posX-(width/2),posY-(height/2)),
								  bottomRight=(posX+(width/2),posY+(height/2)),mass=mass)
		self.type="box"
		self.box=sf.RectangleShape()
		self.box.origin=(width/2,height/2)
		self.box.size=(width,height)
		self.box.position=(posX,posY)
		self.box.fill_color=color
		self.box.outline_color=oColor
		self.box.outline_thickness=oThick
	def updateBounds(self):
		self.center=self.box.position
		self.topLeft=(self.center[0]-(self.box.size[0]/2),self.center[1]-(self.box.size[1]/2))
		self.bottomRight=(self.center[0]+(self.box.size[0]/2),self.center[1]+(self.box.size[1]/2))
	def changeColor(self,nColor): 
		self.box.fill_color=nColor
	def changeOColor(self, nOColor):
		self.box.outline_color=nOColor
	def changeOThick(self, nThick):
		self.box.outline_thickness=nThick
	def setPos(self,pVec):
		self.box.position=pVec
		self.updateBounds()
	def setPos(self,xCoord,yCoord):
		self.box.position.x=xCoord
		self.box.position.y=yCoord
		self.updateBounds()
	def move(self,mVec):
		self.box.position+=mVec
		self.updateBounds()
	def rotate(self,theta):
		self.box.rotate(theta)

class circle(physObject):
	def __init__(self, radius=25,posX=0,posY=0,color=sf.Color.RED,oColor=sf.Color.BLACK,
				 oThick=1,mass=10):
		super(circle,self).__init__(size=(radius*2,radius*2),topLeft=(posX-radius,posY+radius),
									bottomRight=(posX+radius,posY-radius),mass=mass)
		self.type="circle"
		self.circle=sf.CircleShape()
		self.circle.radius=radius
		self.circle.origin=(radius,radius)
		self.circle.position=(posX,posY)
		self.circle.fill_color=color
		self.circle.outline_color=oColor
		self.circle.outline_thickness=oThick
	def updateBounds(self):
		self.center=self.circle.position
		self.topLeft=(self.center[0]-self.circle.radius,self.center[1]-self.circle.radius)
		self.bottomRight=(self.center[0]+self.circle.radius,self.center[1]+self.circle.radius)
	def changeColor(self,nColor):
		self.circle.fill_color=nColor
	def changeOColor(self,nOColor):
		self.circle.outline_color=nOColor
	def changeOThick(self,nThick):
		self.circle.outline_thickness=nThick
	def setPos(self,pVec):
		self.circle.position=pVec
		self.updateBounds()
	def move(self,mVec):
		self.circle.position+=mVec
		self.updateBounds()

class scene(object):
	def __init__(self,windowWidth,windowHeight,title,color,icon=None):
		self.color=color
		#if windowWidth>win32api.GetSystemMetrics(0) or windowHeight>win32api.GetSystemMetrics(1):
		#	print ("Window is too large")
		#	sys.exit()
		self.windowSize=sf.Vector2(windowWidth,windowHeight)
		self.window=sf.RenderWindow(sf.VideoMode(self.windowSize[0],self.windowSize[1]),title)
		if icon != None:
			self.window.icon=icon.pixels
		self.window.framerate_limit=60
		self.objects=[]
	def initLine(self,lpoint,rpoint):
		self.objects.append(line(lpoint,rpoint))
	def initBox(self,width,height,posX,posY,color,oColor,oThick,mass):
		self.objects.append(box(width,height,posX,posY,color,oColor,oThick,mass))
	def initCircle(self,radius,posX,posY,color,oColor,oThick,mass):
		self.objects.append(circle(radius,posX,posY,color,oColor,oThick,mass))
	def initPoly(self):
		pass
	def draw(self,drawObject=None,mVec=(0,0)): # draws the inputted object and moves it
		if drawObject==None:
			return
		elif drawObject.type in ("line","box","circle","poly"):
			drawObject.move(mVec)
			if drawObject.type=="line":
				self.window.draw(drawObject.line)
			if drawObject.type=="box":
				self.window.draw(drawObject.box)
			if drawObject.type=="circle":
				self.window.draw(drawObject.circle)
			if drawObject.type=="poly":
				self.window.draw(drawObject.poly)
	def resize(self):
		if self.window.size != self.windowSize:
			print ("CHANGED")
			self.windowSize=self.window.size

