# Dora Jambor
# Interview prep: Is the string a paindrome?
# Iterative version

def is_palindrome(word):
	if len(word) <= 1:
		return True
	else:
		front = 0
		end = len(word) - 1
		while front < end:
			if word[front] == word[end]:
				front += 1
				end -= 1
			else:
				return False
		return True

# test
print is_palindrome('dora')
print is_palindrome('d')
print is_palindrome('dood')
print is_palindrome('drard')