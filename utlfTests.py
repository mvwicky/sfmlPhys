import sfml as sf
import sys
import os
import random
import math
import utilFunctions as utlF

def main():

	utlF.clear()

	lVec=[]
	tVec=()
	sfVec=sf.Vector2(0,0)
	sf3Vec=sf.Vector3(0,0,0)
	iVec=0
	print(utlF.vecCheck(lVec))
	print(utlF.vecCheck(tVec))
	print(utlF.vecCheck(sfVec))
	print(utlF.vecCheck(sf3Vec))

if __name__=='__main__':
	main()