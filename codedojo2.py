# Chandra and Dora
# May 2016

'''
'Bob decided to pass a very large integer n to Alice. First,
he wrote that number as a string, then, magically, all the
numbers were shuffled in arbitrary order while this note was
passed to Alice. The only thing that Bob remembers is a
non-empty substring of n (a substring of n is a sequence of
consecutive digits of the number n).
Bob knows that there may be more than one way to restore the
number n. Your task is to find the smallest possible initial
integer n. Note that decimal representation of number n contained
no leading zeroes, except in the case the integer n was equal to
zero itself (in this case a single digit 0 was used).
INPUT
The first line of the input contains the string received by
Alice. The number of digits in this string does not exceed
1 000 000.
The second line contains the substring of n which Bob
remembers. This string can contain leading zeroes.
It is guaranteed that the input data is correct, and the answer
always exists.
OUTPUT
Print the smalles integer n which Bob could pass to Alice.
TEST CASES
("3214", "23") -> 1234
("3214", "32") -> 1324
("00312", "021") -> 30021
("9996663330", "63") -> 3036366999
("9996663330", "36") -> 3033666999
'''


A = '898311110'
B = '0'
# 4111830059

def construct(scramble, substr):
    subDict = {}
    numDict = {}
    lenNum = s
    for e in substr:
        if e not in subDict:
            subDict[e] = 1
        else:
            subDict[e] += 1
            
    for e in scramble:
        if subDict.get(e,0) > 0:
            subDict[e] -= 1
        elif e not in numDict:
            numDict[e] = 1
        else:
            numDict[e] += 1
    
    print subDict, numDict 
    return subDict, numDict

def construct_result(scramble, substr):
    subDict, numDict = construct(scramble, substr)
    start = ''
    end = ''
    digitList = ['1', '2', '3','4','5','6','7','8','9']
    for e in digitList:
        num = numDict.get(e, 0)
        if e <= substr[0]:
            start += e * num
        else:
            end += e * num
    numOfZeros = numDict.get('0', 0)
    if substr[0] == '0':
        return end[0] + '0' * numOfZeros + substr + end[1:]
    if len(start) != 0:
        return start[0] + '0' * numOfZeros + start[1:] + substr + end
    else:
        return substr + '0' * numOfZeros + end

print construct_result(A,B)
