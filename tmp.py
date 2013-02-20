number = 110011
palindrome = True
for c in range(0, len(str(number))):
	firstNumToCompare = c
	secondNumToCompare = len(str(number)) - (c+1)
	if secondNumToCompare - firstNumToCompare > 0:
		if str(number)[secondNumToCompare] != str(number)[firstNumToCompare]:
			palindrome = False
			print "Number isn't palindrome!"
			break;

if palindrome == True:
	print "Number is palindrome!"
	
