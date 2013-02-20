from math import sqrt

a = 0
b = 1
c = 1
while (a + b + c) != 1000:
	a += 1
	b = a+1
	while (a+b+c) < 1000:
		b += 1
		c = sqrt(b**2 + a**2)

print a*b*c

