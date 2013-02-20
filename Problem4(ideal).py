largestPalindrome = 0
for a in range (101, 1000):
	firstNumber = 1000 - (a - 100)
	for b in range (101, 1000):
		secondNumber = 1000 - (b - 100)
		sumOfNumbers = firstNumber*secondNumber
		if sumOfNumbers < largestPalindrome:
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
		

print largestPalindrome
