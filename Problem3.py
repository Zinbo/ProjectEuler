primeNumbers = [1, 2, 3, 5, 7, 11]
number = 600851475143
i = 1

def addPrime():
	possiblePrime = primeNumbers[len(primeNumbers) - 1] + 1
	found = False
	while not(found):
		if isPrime(possiblePrime):
			primeNumbers.append(possiblePrime)
			found = True
		else:
			possiblePrime += 1

def isPrime(numberToCheck):
	divisorFound = False
	factor = 2
	divisor = 3 #Arbitrary number, gets replaced immediately
	while divisorFound == False and divisor > 2:
			divisor = numberToCheck / factor
			if numberToCheck % divisor == 0:
				divisorFound = True
			factor += 1
	return not(divisorFound)	


while isPrime(number) == False:
	while not(number % primeNumbers[i] == 0):
		i += 1
		if i >= len(primeNumbers):
			addPrime()
	number = number / primeNumbers[i]

print "Biggest prime factor: %i"%(number)
