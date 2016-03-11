# Dora Jambor
# Interview prep: Is the string a paindrome?

def is_palindrome(word):
	if len(word) <= 1:
		return True
	else:
		front = 0
		end = len(word) - 1
		if word[front] == word[end]:
			is_palindrome(word[1:-1])
		else:
			return False
		return True


print is_palindrome('dora')
print is_palindrome('d')
print is_palindrome('dood')
print is_palindrome('drard')