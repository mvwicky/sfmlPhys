#
# file for testing the matrixFuncs and vecFuncs libraries
#
import matrixFuncs as mF 
import vecFuncs as vF 
import os

def clear():
	os.system('cls')

def pause():
	os.system('pause')


def main():
	clear()
	print('')
	m1=mF.createSquareMatrix(5)
	m2=mF.createSquareMatrix(5,True)
	m3=mF.createSquareMatrix(5)

	mF.printMatrix(m1)
	print("")
	mF.printMatrix(m2)
	print("")
	mF.printMatrix(m3)
	

if __name__ == '__main__':
	main()
