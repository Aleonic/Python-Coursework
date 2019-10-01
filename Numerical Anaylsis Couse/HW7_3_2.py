import numpy as np
import matplotlib as plt

x = [2.95, 1.74, -1.45, 1.32]

x1_r = [0, 1.23, 4.45, 1.61]
x2_r = [-1.23, 0, 3.21, 0.45]
x3_r = [-4.45, -3.21, 0, -2.75]
x4_r = [-1.61, -0.45, 2.75, 0]

b = [0, 0, 0, 0]
b[0] = [x[0], x1_r[1] + x[1], x1_r[2] + x[2], x1_r[3] + x[3]]
b[1] = [x[1], x2_r[0] + x[0], x2_r[2] + x[2], x2_r[3] + x[3]]
b[2] = [x[2], x3_r[0] + x[0], x3_r[1] + x[1], x3_r[3] + x[3]]
b[3] = [x[3], x4_r[0] + x[0], x4_r[1] + x[1], x4_r[2] + x[2]]

x_axis = np.array([0,1,2,3])
m = [0,0,0,0]
c = [0,0,0,0]

A = np.vstack([x_axis, np.ones(len(x))]).T

m[0], c[0] = np.linalg.lstsq(A, b[0], rcond=None)[0]
m[1], c[1] = np.linalg.lstsq(A, b[1], rcond=None)[0]
m[2], c[2] = np.linalg.lstsq(A, b[2], rcond=None)[0]
m[3], c[3] = np.linalg.lstsq(A, b[3], rcond=None)[0]

for i, val in enumerate(c):
	print("Original x{} = {}".format(i+1, x[i]))
	print("Estimated x{} = {}".format(i+1, val))
	print("Difference to original measurement: {} \n".format(abs(x[i] - val)))