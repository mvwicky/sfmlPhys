import sys
import os
import random
import math

#class utl(object):
#	def __init__(self,framerate):
#		self.g=98.1
#		self.dt=float(1)/float(framerate)
#	def calcForces(self,bottom,xnot,floor,fVec):
#		pass

def vecCheck(tVec, types=None):
	if types==None:
		if type(tVec) in (tuple,list):
			return True
		else:
			return False
	elif types!=None:
		if type(tVec) in types:
			return True
		else: 
			return False

def inVPlane(xCoord,tL,bR): # tL and bR should be the top left and bottom right 
							# coordinates of the object
	if (xCoord>=tL[0] and xCoord<=bR[0]):
		return True
	else:
		return False

def inHPlane(yCoord,tL,bR): # tL and bR should be the top left and bottom right 
							# coordinates of the object
	if (yCoord>=tL[1] and yCoord<=bR[1]):
		return True
	else:
		return False

def pointIn(pVec,tL,bR): # tL and bR should be the top left and bottom right 
						 # coordinates of the object
	if inVPlane(pVec[0],tL,bR) and inHPlane(pVec[1],tL,bR):
		return True
	else:
		return False

def createCorners(center,height,width):
	tL=[center[0]-height/2,center[1]-width/2]
	bR=[center[0]+height/2,center[1]+width/2]
	return [tL,bR]

def ccwReOrder(pVec):
	for i in range(len(pVec)):
		pass

def cwReOrder(pVec):
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