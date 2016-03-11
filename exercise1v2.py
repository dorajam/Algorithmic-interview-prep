try1 = 'abcd'
try2 =  'abb'
try3 = 'zszd'

def uniqueStr(word):
    checker = 0
    for i in range(len(word)):
       dif = ord(word[i]) - ord('a')
       if checker & (1 << dif) > 0:
           return False
       checker |= (1 << dif)
    return True


print uniqueStr(try1)
print uniqueStr(try2)
print uniqueStr(try3)