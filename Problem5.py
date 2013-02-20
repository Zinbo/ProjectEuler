eighteen = [2, 3, 6, 9, 18]
sixteen = [2, 4, 8]
fifteen = [3, 5]
fourteen = [2, 7]
twelve = [2, 4, 6]

multiples = {18:[2, 3, 6, 9, 18],  17:[17], 16:[2, 4, 8, 16], 15:[3, 5, 15],
14:[2, 7, 14], 13:[13], 12:[2, 4, 6], 11:[11]}
smallestNumber = 20*19
numberToDiviseBy = 18
while numberToDiviseBy > 10:
	index = 0
	if smallestNumber % numberToDiviseBy == 0:
		numberToDiviseBy -= 1
	else:
		for multiple in multiples[numberToDiviseBy]:
			tmpSmallestNumber = smallestNumber * multiple
			if tmpSmallestNumber % numberToDiviseBy == 0:
				smallestNumber = tmpSmallestNumber
				numberToDiviseBy -= 1
				break

print smallestNumber
