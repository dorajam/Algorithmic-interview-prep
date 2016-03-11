# Python dictionaries are implemented as hash tables -> O(1) constant time
# extra space is everything stored in dict -> O(n)

try1 = 'abcd'
try2 =  'abb'
try3 = 'zszd'

def uniqueStr(word):
    check = {}
    for c in word:
        if check.get(c, 0) == 0:
            check[c] = 1
        else:
            return False
    return True

print uniqueStr(try1)
print uniqueStr(try2)
print uniqueStr(try3)