import math
import utilFunctions as utlF
#
# a library for manipulating vectors (nx1 matricies)
#

def dotProduct(a,b): # returns the dot product of two vectors a and b
	if len(a)!=len(b):
		print ("vectors are not the same length")
		return -1
	elif len(a)==len(b):
		dot=float(0)
		for i in range(len(a)):
			dot+=a[i]*b[i]
		return dot


def crossProduct(a,b): # returns the cross product of two vectors a and b 
					   # (only works for 3x3 right now)
					   # returned as a tuple
	pass

#class vector(list):
#	def __init__(self,n):
#		iVec=[]
#		for i in range(n):
#			iVec.append(0)
#		super(vector,self).__init__(iVec)
#	def dotProduct(self, b):
#		pass

