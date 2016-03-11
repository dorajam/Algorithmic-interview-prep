import numpy as np


try1 = 'abcd'
try2 =  'abb'
try3 = 'zszd'

def uniqueStr(word):
    lookup = np.zeros((127), dtype=bool)
    for c in word:
        dif = ord(c) - ord('a')
        if lookup[dif]:
            return False
        else:
            lookup[dif] = True
    return True


print uniqueStr(try1)
print uniqueStr(try2)
print uniqueStr(try3)