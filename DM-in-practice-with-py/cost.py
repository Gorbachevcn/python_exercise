import math
from math import pi
a=[1,2,3]
b=[]
for x in a:
     b.append(x+1)

print a
print b
c=[i+3 for i in a]
print c

f = lambda x : math.sin(x)
print f(pi/2)

q = map(lambda x:x**2,a)
print q
