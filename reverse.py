# reverse a C-style string
# n function calls
# space complexity could be O(n) if reverse(word[1:]) doesnt create a copy of word, it just creates a pointer at a new memory location pointing at the substring
# time complexity is n squared -> n(n/2)  - n/2 is average number of copying operation

a = 'dora'

def reverse(word):
    if len(word) == 1:
        return word
    else:
        return str(reverse(word[1:]))+word[0]

# print reverse(a)

#
# def reverse1(word):
#     front = 0
#     end = -1
#     while front < end:
#         tmp = word[front]
#         word[front] = word[end]
#         word[end] = tmp
#         front += 1
#         end -= 1
#     print word
#
# reverse1(a)