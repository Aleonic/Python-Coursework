# 2.2(3)
import math

def fp1(x):
	return 1/(2*math.sqrt(x+1))

def fp2(x):
	return 1/(math.pow(x,2)+1)

def fp3(x):
	return math.pi*math.cos(math.pi*x)

def fp4(x):
	return math.pow(-1*math.e,-x)

def fp5(x):
	return 1/x

def f1(x):
	return math.sqrt(x+1)

def f2(x):
	return math.atan(x)

def f3(x):
	return math.sin(math.pi * x)

def f4(x):
	return math.pow(math.e,-x)

def f5(x):
	return math.log(x)

x = 1
h = 4
print("Question 2.2: #3 on python")
print("---------Part A---------")
while h <= (32):
	single_appr = ((f1(x+(1/h)) - f1(x))/(1/h))
	double_appr = ((f1(x+(1/h)) - f1(x - (1/h)))/(2/h))

	single_err = math.fabs(fp1(x) - single_appr)
	double_err = math.fabs(fp1(x) - double_appr)
	print("x =",x,"h= 1 /",h)
	print("Single approximation =",single_appr, "Error =", single_err)
	print("Double approximation =",double_appr, "Error =", double_err)
	h = h * 2

print()
h = 4
print("---------Part B---------")
while h <= (32):
	single_appr = ((f2(x+(1/h)) - f2(x))/(1/h))
	double_appr = ((f2(x+(1/h)) - f2(x - (1/h)))/(2/h))

	single_err = math.fabs(fp2(x) - single_appr)
	double_err = math.fabs(fp2(x) - double_appr)
	print("x =",x,"h= 1 /",h)
	print("Single approximation =",single_appr, "Error =", single_err)
	print("Double approximation =",double_appr, "Error =", double_err)
	print()
	h = h * 2

print()
h = 4
print("---------Part C---------")
while h <= (32):
	single_appr = ((f3(x+(1/h)) - f3(x))/(1/h))
	double_appr = ((f3(x+(1/h)) - f3(x - (1/h)))/(2/h))

	single_err = math.fabs(fp3(x) - single_appr)
	double_err = math.fabs(fp3(x) - double_appr)
	print("x =",x,"h= 1 /",h)
	print("Single approximation =",single_appr, "Error =", single_err)
	print("Double approximation =",double_appr, "Error =", double_err)
	print()
	h = h * 2

print()
h = 4
print("---------Part D---------")
print("Part D:")
while h <= (32):
	single_appr = ((f4(x+(1/h)) - f4(x))/(1/h))
	double_appr = ((f4(x+(1/h)) - f4(x - (1/h)))/(2/h))

	single_err = math.fabs(fp4(x) - single_appr)
	double_err = math.fabs(fp4(x) - double_appr)
	print("x =",x,"h= 1 /",h)
	print("Single approximation =",single_appr, "Error =", single_err)
	print("Double approximation =",double_appr, "Error =", double_err)
	print()
	h = h * 2

print()
h = 4
print("---------Part E---------")
print("Part E:")
while h <= (32):
	single_appr = ((f5(x+(1/h)) - f5(x))/(1/h))
	double_appr = ((f5(x+(1/h)) - f5(x - (1/h)))/(2/h))

	single_err = math.fabs(fp5(x) - single_appr)
	double_err = math.fabs(fp5(x) - double_appr)
	print("x =",x,"h= 1 /",h)
	print("Single approximation =",single_appr, "Error =", single_err)
	print("Double approximation =",double_appr, "Error =", double_err)
	print()
	h = h * 2