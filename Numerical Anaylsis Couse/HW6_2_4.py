import scipy
import scipy.linalg
import numpy as np
import itertools

collectC = np.array(list(itertools.product([-1,1],repeat = 3)))

matrixA = np.array([[10,-7,0],[-3,2,6],[5,-1,5]])
matrixB = np.array([[-73,78,24],[92,66,25],[-80,37,10]])

aT = matrixA.transpose();
aP, aL, aU = scipy.linalg.lu(aT);

bT = matrixB.transpose();
bP, bL, bU = scipy.linalg.lu(bT);

aUT = aU.transpose();
bUT = bU.transpose();
aLT = aL.transpose();
bLT = bL.transpose();

maxVA = np.array([0,0,0])
maxVB = np.array([0,0,0])

for c in collectC:
	testA = np.linalg.solve(aUT,c)
	testB = np.linalg.solve(bUT,c)
	
	if(np.linalg.norm(maxVA) < np.linalg.norm(testA)):
		maxVA = testA

	if(np.linalg.norm(maxVB) < np.linalg.norm(testB)):
		maxVB = testB

yA = np.linalg.solve(aLT,maxVA)
yB = np.linalg.solve(bLT,maxVB)

zA = np.linalg.solve(matrixA,yA)
zB = np.linalg.solve(matrixB,yB)

invA = np.linalg.norm(zA) / np.linalg.norm(yA)
invB = np.linalg.norm(zB) / np.linalg.norm(yB)

condA = np.linalg.norm(matrixA) * invA
condB = np.linalg.norm(matrixB) * invB
realCA = np.linalg.cond(matrixA)
realCB = np.linalg.cond(matrixB)

print(matrixA)
print('Cond(A) 1-norm real = {}' .format(realCA))
print('Cond(A) 1-norm appr = {}' .format(condA))

print(matrixB)
print('Cond(B) 1-norm real = {}' .format(realCB))
print('Cond(B) 1-norm appr = {}' .format(condB))
