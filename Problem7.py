primeNumbers = [2, 3, 5, 7, 11]

def isPrime(numberToCheck):
	divisorFound = False
	factor = 2
	divisor = 3 #Arbitrary number, gets replaced immediately
	if numberToCheck % 2 == 0:
		return False
	while divisorFound == False and divisor > 2:
			divisor = numberToCheck / factor
			if numberToCheck % divisor == 0:
				divisorFound = True
			factor += 1
	return not(divisorFound)	

while len(primeNumbers) != 10001:
	possiblePrime = primeNumbers[len(primeNumbers) - 1] + 1
	found = False
	while not(found):
		if isPrime(possiblePrime):
			primeNumbers.append(possiblePrime)
			found = True
		else:
			possiblePrime += 1

print primeNumbers[10000]
