sumOfNumbers = 0
sumOfSquares = 0
for i in range(1, 101):
	sumOfNumbers += i
	sumOfSquares += i**2



print abs(sumOfNumbers**2 - sumOfSquares)
