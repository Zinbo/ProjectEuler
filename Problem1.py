sumOfMultiples = 0
inBothMultiples = 0

numberOfFiveMultiples = 0

for i in range(1, (1000/5)):
	multiple = 5*i
	sumOfMultiples += multiple
	numberOfFiveMultiples += 1
	if (multiple % 3 == 0):
		inBothMultiples += multiple


for i in range(1, 334):
	sumOfMultiples += 3*i

print "Sum of multiples of 5 and 3 less than 1000:  %i" % (sumOfMultiples - inBothMultiples)
