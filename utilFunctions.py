import sys
import os
import random
import math
from enum import Enum
from sfml import Vector2
from sfml import Vector3
from sfml import Color

class direction(Enum):
	left=1
	up=2
	right=3
	down=4

def clear():
	if sys.platform=='win32':
		os.system('cls')
	else:
		print("Not Windows")

def pause(): 	
	if sys.platform=='win32':
		os.system('pause')
	else:
		print("Not Windows")

def vecCheck(tVec, types=(tuple,list,Vector2,Vector3)): 
# makes sure the inputted vector are a certain type
	if type(tVec) in types:
		return True
	else:
		return False

def typeCheck(input,types):
	if type(input) in types:
		return True
	else:
		return False

def inVPlane(xCoord,tL,bR): # tL and bR should be the top left and bottom right 
							# coordinates(bounds) of the object
	if vecCheck(tL) and vecCheck(bR):
		if (xCoord>=tL[0] and xCoord<=bR[0]):
			return True
		else:
			return False
	elif not vecCheck(tL) and not vecCheck(bR):
		print("Types are wrong")
		return False


def inHPlane(yCoord,tL,bR): # tL and bR should be the top left and bottom right 
							# coordinates(bounds) of the object
	if vecCheck(tL) and vecCheck(bR):
		if (yCoord>=tL[1] and yCoord<=bR[1]):
			return True
		else:
			return False
	elif not vecCheck(tL) and not vecCheck(bR):
		print("Types are wrong")
		return False

def pointIn(pVec,tL,bR): # tL and bR should be the top left and bottom right 
						 # coordinates(bounds) of the object
	if vecCheck(tL) and vecCheck(bR):
		if inVPlane(pVec[0],tL,bR) and inHPlane(pVec[1],tL,bR):
			return True
		else:
			return False
	elif not vecCheck(tL) and not vecCheck(bR):
		print("Types are wrong")
		return False

def createCorners(center,width,height=None): 
# creates the corners (top left and bottom right) of an object based on center and size
	if height==None and vecCheck(width): 
		# if width==[width,height]
		tL=[center[0]-width[1]/2,center[1]-width[0]/2]
		bR=[center[0]+width[1]/2,center[1]+width[0]/2]	
		return [tL,bR]	
	elif width!=None:
		tL=[center[0]-height/2,center[1]-width/2]
		bR=[center[0]+height/2,center[1]+width/2]
		return [tL,bR]
	

def ccwReOrder(pVec): # TODO
# orders the points in pVec in a counter clockwise fashion	
	rightMost=pVec[0] # makes the first coordinate the right-most
	rightMostInd=0
	ccwVec=[]
	for i in range(len(pVec)): # finds the rightmost
		if (pVec[i][0]>=rightMost[0])and(pVec[i][1]>rightMost[1]):
		# if the next point it further right and further up
			rightMost=pVec[i]
			rightMostInd=i
	ccwVec.append(rightMost)
	del pVec[rightMostInd]




def cwReOrder(pVec): # TODO
# orders the points in pVec in a clockwise fashion
	for i in range(len(pVec)): # x coordinate
		pass

def calcHeight(pVec): # TODO
# calculates the average (y-axis) of a poly based on its points
	for i in range(len(pVec)):
		pass

def calcWidth(pVec): # TODO
# calculates the average width(x-axis) of a poly based on its points
	for i in range(len(pVec)):
		pass

def degToRad(deg):
	return deg*(math.pi/180)

def radToDeg(rad):
	return rad*(180/math.pi)

def calcLength(sPoint,ePoint):
	return math.sqrt((sPoint[0]-ePoint[0])**2(sPoint[1]-ePoint[0])**2)

def calcSlope(sPoint,ePoint):
	return (sPoint[1]-ePoint[1])/(sPoint[0]-ePoint[0])

def calcAngleRad(sPoint,ePoint):
	return math.atan((sPoint[1]-ePoint[1])/(sPoint[0]-ePoint[1]))

def calcAngleDeg(sPoint, ePoint):
	return radToDeg(calcAngleRad(sPoint,ePoint))

def getDefaultArgs(windowWidth,windowHeight): 
# returns an array that contains default arguments for the shapes
	size=(50,50)
	position=(windowWidth/2,windowHeight/2)
	color=Color.RED
	oColor=Color.BLACK
	oThick=1
	mass=10
	return [size,position,color,oColor,oThick,mass]

def calcCurMaxHeight(springConstant,numBounces):
	return (springConstant*((numBounces+3)))