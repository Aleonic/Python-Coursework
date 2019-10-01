import math 
import matplotlib.pyplot as plt

def epsilon():
	x =0.5
	while (1+x != 1):
		x = x/2

	return (x * 2)

x = 1 
h = [] # variable to store h values
err = [] # variable to store error for h

for k in range(0,49): 
   h = h+[1/math.pow(2,k+1)] # calculate h
   f_prime = (math.sin(x+h[k])-math.sin(x))/h[k]# find derivative
   err = err +[math.fabs(f_prime-math.cos(x))]# Calculate error

plt.plot(h,err)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h value')
plt.ylabel('Error value')
plt.show() # plot graph

for k in range(0,49): # find h with minimum err
   if err[k] == min(err):
       H = h[k]
       
RoTH = math.sqrt(epsilon()) * math.fabs(x) # rule of thumb
print("h for minumum error= {}" .format(H))
print("Rule of Thumb h = {}" .format(RoTH))