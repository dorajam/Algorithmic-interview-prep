# Dora Jambor
# Inteview Preparation from "Cracking the coding interview" book
# Exercise

'''
Replace space characters by %20, you may assume that the string has sufficient space at the end of 
the string to hold he additional characters and that you're given the true length of string.
'''

word = 'Ms Dora Jambor'

def changeSpace(str1):
	count = 0
	length = len(str1)
	for c in str1:
		if c == ' ':
			count += 1
	length += count
	for i in range(0,length,-1):
		if str1(i) == ' ':
			str1[length - 1] = '0'
			str1[length - 2] = '2'
			str1[length - 3] = '%'
			length -= 3
		else:
			str1[length-1] = str1[i]
			print str1[i]

print changeSpace(word)