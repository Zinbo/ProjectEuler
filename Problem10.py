from math import sqrt
from math import ceil

primeNumbers = [2]
newestSuspect = 3
sumOfPrimes = 0

def isPrime(primeSuspect):
	if primeSuspect % 2 == 0:
		return False
	divider = 3
	stoppingPoint = ceil(sqrt(primeSuspect))
	while divider <= stoppingPoint:
		if primeSuspect % divider == 0:
			return False
		divider += 1
	return True

while newestSuspect < 2000000:
	if isPrime(newestSuspect):
		primeNumbers.append(newestSuspect)
	newestSuspect += 1

print "last prime: %i"%primeNumbers[-1]

for i in range(0, len(primeNumbers)):
	sumOfPrimes += primeNumbers[i]

print sumOfPrimes
