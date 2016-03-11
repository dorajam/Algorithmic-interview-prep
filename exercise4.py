# Dora Jambor
# Inteview Preparation from "Cracking the coding interview" book
# Exercise

'''
Replace space characters by %20, you may assume that the string has sufficient space at the end of 
the string to hold he additional characters and that you're given the true length of string.
'''

word = 'Ms Dora Jambor'

def changeSpace(str1):
	makeList = list(str1)
	print makeList
	for i in range(len(makeList)):
		if makeList[i] == ' ':
			makeList[i] = '%20'
	return "".join(makeList)

print changeSpace(word)