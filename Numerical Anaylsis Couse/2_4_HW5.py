import numpy as np

matrixA = np.array([[10,-7,0],[-3,2,6],[5,-1,5]])
matrixB = np.array([[-73,78,24],[92,66,25],[-80,37,10]])

randY = []

for i in range(0,30000):
	randY = randY + [np.random.randint(-100,100, size=3)]

collectZA = []
collectZB = []

for k in randY:
	collectZA = collectZA +[np.linalg.solve(matrixA,k)]
	collectZB = collectZB +[np.linalg.solve(matrixB,k)]

maxRA = -1
maxRB = -1

for i in range(0,30000):

	ratio1 = np.linalg.norm(collectZA[i]) / np.linalg.norm(randY[i])
	ratio2 = np.linalg.norm(collectZB[i]) / np.linalg.norm(randY[i])
	
	if ratio1 > maxRA:
		maxRA = ratio1

	if ratio2 > maxRB:
		maxRB = ratio2

condA = np.linalg.norm(matrixA) * maxRA
condB = np.linalg.norm(matrixB) * maxRB
realCA = np.linalg.cond(matrixA)
realCB = np.linalg.cond(matrixB)

print(matrixA)
print('Cond(A) 1-norm real = {}' .format(realCA))
print('Cond(A) 1-norm appr = {}' .format(condA))

print(matrixB)
print('Cond(B) 1-norm real = {}' .format(realCB))
print('Cond(B) 1-norm appr = {}' .format(condB))