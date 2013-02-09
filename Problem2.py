oldFibNum = 1
currentFibNum = 2
sumOfEvenFibNums = 0

while currentFibNum < 4000000:
	if currentFibNum % 2 == 0:
		sumOfEvenFibNums += currentFibNum
	tmpFibNum = currentFibNum
	currentFibNum += oldFibNum
	oldFibNum = tmpFibNum

print "Sum of even fibonacci numbers less than 4 million: %i"%(sumOfEvenFibNums)
