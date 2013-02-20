largestPalindrome = 0
db = 1
a = 999
b = 999

while a >= 100:
	if a % 11 == 0:
		b = 999		
		db = 1
	else:
		b = 990
		db = 11
	while b >= 100:
		sumOfNumbers = a * b
		if sumOfNumbers <= largestPalindrome:
			break
		isPalindrome = True
		startIndex = 0
		endIndex = len(str(sumOfNumbers)) - 1
		while (endIndex - startIndex) > 0:
			if str(sumOfNumbers)[startIndex] != str(sumOfNumbers)[endIndex]:
				isPalindrome = False
				break
			startIndex += 1
			endIndex -= 1
		if isPalindrome and (sumOfNumbers > largestPalindrome):
			largestPalindrome = sumOfNumbers
		b -= db
	a -= 1

print largestPalindrome
