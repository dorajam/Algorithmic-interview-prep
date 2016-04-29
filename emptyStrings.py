# given an sorted array of strings (with random empty strings in the list), find the location of a given string
# Dora Jambor April 2016

# given the array is sorted, you can use binary search
def finder(ls, s, low_index, high_index):
    mid = int((low_index + high_index)/2)
    if len(ls) == 1 and ls[0] != s:
        return -1
    if ls[mid] == s:
        return mid
    if ls[mid] < s:
        return finder(ls, s, mid+1, len(ls))
    if ls[mid] > s:
        return finder(ls, s, 0, mid)
    if ls[mid] == "":
        a = finder(ls, s, mid+1, len(ls))
        b = finder(ls,s, 0, mid)
        if a == -1 and b == -1:
            return -1
        if a != -1:
            return a
        else:
            return b


a = ["ab", "", "ba", "ca","","","", "da", "xa"]
print finder(a, "xa",0, len(a))
