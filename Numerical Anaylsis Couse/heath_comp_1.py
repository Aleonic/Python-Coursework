import math
def stir(n):
	return math.sqrt(2 * math.pi * n) * math.pow(n/math.e, n)

i = 1
while (i < 11):
	Av = math.factorial(i)
	Ev = stir(i)
	Abs_err = abs(Ev - Av)
	Rel_err = Abs_err/Av
	print("Absolute error = {} , Relative error = {}" .format(Abs_err, Rel_err))
	i = i + 1