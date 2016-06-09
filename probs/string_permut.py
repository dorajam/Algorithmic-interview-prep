# Find all permutations of a string

'''
'a' -> all permutations of length (n-1) + dont start with 'a' -> 'b'
'b' -> all permuts -> glue

'abc' -> take 'a' -> find all permuts: 'bc', 'cb' (dont include first element) -> 'abc', 'acb'
      -> take 'b' -> 'ac', 'ca' -> 'bac', 'bca'
      -> take 'c' -> 'ab', 'ba'-> 'cab', 'cba'
'''
def permut(s):
    if len(s) <= 1:
        return [s]

    res =[]
    for i in range(len(s)):
        list_chars = list(s)
        list_chars.pop(i)
        subres = [s[i] + sub for sub in permut(''.join(list_chars))]
        res += subres
    return res

res =  permut('abc')
print res
