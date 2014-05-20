#
# a library with functions mxn sized matrices
# includes special functions for square matrices
#
# matrices are lists, dimensions are tuples
# matrices can be converted to tuples(for some reason)
#
# m is used for rows, n is used for columns
# 
# 

def createMatrix(m,n): # returns an empty(zero filled) mxn sized matrix
	tMat=[]
	for i in range(m):
		tMat.append([])
		for j in range(n):
			tMat[i].append(0)
	return tMat

def createSquareMatrix(m, ident=False): # returns an empty(zero filled) mxm matrix
	if ident==False:
		tMat=createMatrix(m,m)
		return tMat
	elif ident==True:
		tMat=[]
		for i in range(m):
			tMat.append([])
			for j in range(m):
				if i==j:
					tMat[i].append(1)
				else:
					tMat[i].append(0)
		return tMat

def size(mat): # returns the size of the inputted matrix as a tuple=(m,n)
	return (len(mat), len(mat[0]))

def printMatrix(mat): # prints out the matrix in a nicer style
	for i in range(len(mat)):
		print (mat[i])

def det(mat): # returns the determinant of a square matrix
	if size(mat)[0]!=size(mat)[1]:
		print ("not a square matrix")
		return -1
	elif size(mat)[0]==size(mat)[1]:
		pass

def replaceRow(mat,i, nRow): # replaces the ith row of mat with nRow
	#if size(mat)[0]>i:
	#	print ("matrix is too big")
	#	return mat[i]
	if size(mat)[1]!=len(nRow):
		print ("new row is not the correct size")
		return mat[i]
	mat[i]=nRow
	return mat

def replaceColumn(mat, j, nCol): # replaces the jth columns of mat with cCol
	pass


#

def multiply(a,b): # returns the multiplication of matrices a and b
				   # returns as a list of lists(like normal)
				   # checks if the matrices are the correct size first
	if size(a)[1]!=size(b)[0]:
		print ("vectors are not of proper size")
		return -1
	elif size(a)[1]==size(b)[0]:
		print ("proper size")
