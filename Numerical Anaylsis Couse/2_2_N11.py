import math
from fractions import Fraction

def f(x):
	return math.atan(x)

def f_p(x):
	return 1/(math.pow(x,2) + 1)

oldApprox = 0
h = 0.5

while True:
	newApprox = ((8*f(0.25 * math.pi + h) - 8*f(0.25 * math.pi - h) - f(0.25 * math.pi + (2 * h)) + f(0.25 * math.pi - (2 * h))) / (12*h))
	errround = math.fabs(round(newApprox,8) - newApprox)
	errmath = math.fabs(f_p(0.25*math.pi) - newApprox)
	print("h =",h, "Round Error =", errround, "Math error =", errmath)

	if (errround > errmath):
		print("Smallest value of h is", Fraction(h))
		break
	else:
		oldApprox = newApprox
		h = h / 2