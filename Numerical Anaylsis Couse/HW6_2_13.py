import scipy
import scipy.linalg
import numpy as np

def findDiagDet(A):
	aP, aL, aU = scipy.linalg.lu(A);
	dU = aU.diagonal()
	dL = aL.diagonal()

	aT = 1
	bT = 1

	for i in dU:
		aT = aT * i
	for i in dL:
		bT = bT * i

	return aT * bT


matrixA = np.random.randint(-100,100, size=(3,3))

print(matrixA)
print("Real determinant of matrix A = {}" .format(np.linalg.det(matrixA)))
print("Calculated determinant of matrix A = {}" .format(findDiagDet(matrixA)))