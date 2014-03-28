# vectors and matrices tend to be used interchangeably

# createVecs currently doesn't work

import sfml as sf
import random

def lenCheck(vec,length): # checks the input vector is of the inputted length 
	if len(vec)==length:
		return True
	else:
		return False

def vecCheck(*vec): # checks if all input elements are of the same type
	for i in range(1,len(vec)):
		if type(vec[0]) != type(vec[i]):
			return False
	return type(vec[0])

def vecCheck(vec): # checks if all members of the input vector are of the same type
	for i in range(1, len(vec)):
		if (type(vec[0])) != type(vec[i]):
			return False
		return type(vec[0])
	
def sfVec(vec):
	if len(vec)==2:
		return sf.Vector2()+vec
	if len(vec)==3:
		return sf.Vector3()+vec


def vecAdd(*vec): # vectorially adds vectors(row matrices). input is an arbitrary
				  # number of arguments, function adds the corresponding elements
				  # of each vector
	tVec=[]
	rVec=[]
	curInd=0
	for j in range(len(vec)):
		tVec.append(tuple(vec[j]))
	for j in range(len(tVec[0])):
		for i in range(len(tVec)):
			curInd+=tVec[i][j]
		rVec.append(curInd)
		curInd=0
	return tuple(rVec)

def vecAdd(vec): # vectorially adds vectors(row matrices). input is a matrix of
				 # i rows and j columns. adds down the columns. returns a vector 
				 # of size j
	pass

def multiValCheck(vec, val): # checks if more than one element in a row vector
						     # are equal. Returns a tuple containing a fraction of 
						     # the value: (number of element equaling value)/(total elements)
						     # and all the indicies that equal the value
						  	 # e.g. if all elements are equal, the tuple will contain 1, 
						  	 # followed by all matrix indicies
						  	 # e.g. if half of the elements are equal, the tuple will 
						  	 # contain .5, followed by a total of half of the indicies
						  	 # of the matrix
	rTup=[] # returned value (will be converted to a tuple)
	ind=[] # will contain the indicies that contain the value 
	for i in range(len(vec)):
		if vec[i]==val:
			ind.append(i)
	frac=float(len(ind))/float(len(vec))
	rTup.append(frac)
	for i in range(len(ind)):
		rTup.append(ind[i])
	return tuple(rTup)
	
def createVecs(rows, columns, vType=list, seq=True, rand=False, intRand=True, bounds=None, 
			   oneVal=False, val=None, stepVal=False, stepSet=None): 
			   # returns a vector of vectors(a matrix) dictated by:
			   # rows: number of vectors/length of returned vector, 
			   # columns: number of elements per member vector
			   # vType: the type of each row element 
			   # element value flags: dictate what the value of each element will be
			   # 	seq(default): elements go from zero to total number of elements minus 1
			   #	rand: elements have random values
			   #		intRand: True->elements are integers, False->elements are floats
			   #		bounds: two element vector containing the lower and upper bounds for
			   #				the random number
			   #	oneVal: all elements of the matrix have the same value
			   #		val: the value of all elements
			   #	stepVal: the values of elements start at some value and step by some value
			   #		stepSet: two element vector containing lowest number and highest number
	
	# At some point maybe break it into multiple functions

	rVec=[] # the returned vector(will be converted to tuple)

	types={list:[],tuple:(),sf.Vector2:sf.Vector2,sf.Vector3:sf.Vector3}

	flags= [seq,rand,oneVal,stepVal]
	if (multiValCheck(flags,True)[0] != .25):
		flags=[True,False,False,False]

	if vType==sf.Vector2:
		columns=2
	if vType==sf.Vector3:
		columns=3

	if flags[0]==True: # sequential
		num=0
		for i in range(rows):
			rVec.append(types[vType])
			for j in range(columns):
				rVec[i].append(num)
				num+=1
		return tuple(rVec)

	if flags[1]==True: # random values
		if len(bounds) != 2:
			return -1
		if bounds[0] > bounds[1]:
			return -1
		random.seed()
		if intRand==True:
			for i in range(rows):
				rVec.append([])
				for j in range(columns):
					rVec[i].append(random.randint(bounds[0],bounds[1]))
					rVec[i][j]=float(rVec[i][j])
		return tuple(rVec)

		if intRand==False:
			for i in range(rows):
				rVec.append(types[vType])
				for j in range(columns):
					rVec[i].append(random.uniform(bounds[0],bounds[1]))
		return tuple(rVec)
				
	if flags[2]==True: # one value
		for i in range(rows):
			rVec.append(types[vType])
			for j in range(columns):
				rVec[i].append(val)
		return tuple(rVec)

	if flags[3]==True: # stepped values
		num=stepSet[0]
		step=float(stepSet[1]-stepSet[0])/float(rows*columns-1)
		for i in range(rows):
			rVec.append(types[vType])
			for j in range(columns):
				rVec[i].append(num)
				num+=step
		return tuple(rVec)


def printVectors(asMatrix=False,*vec):
	pass

def printVectors(vec,asMatrix=False):
	pass