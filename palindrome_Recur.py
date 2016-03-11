# Dora Jambor
# Interview prep: Is the string a paindrome?

def is_palindrome(word):
	if len(word) <= 1:
		return True
	if word[0] == word[-1]:
		is_palindrome(word[1:-1])
	else:
		return False
	return True

# test
print is_palindrome('dora')
print is_palindrome('d')
print is_palindrome('dood')
print is_palindrome('drard')