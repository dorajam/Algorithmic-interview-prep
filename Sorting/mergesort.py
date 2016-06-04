# Dora Jambor
# June 2016
# Implementation of the merge sort algorithm

# Example of the divide and conquer algo

def merge(arr):
    sorted_list = []
    if len(arr) <= 1:
        return arr
    mid = len(arr)/2
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    compare1 = left[0]
    compare2 = right[0]
    right_index = 0
    left_index = 0
    while True:
        if compare1 <= compare2:
            sorted_list.append(compare1)
            left_index += 1
            if len(left) != left_index:
                compare1 = left[left_index]
            else:
                sorted_list += right[right_index:]
                break
        else:
            sorted_list.append(compare2)
            right_index += 1 
            if len(right) != right_index:
                compare2 = right[right_index]
            else:
                sorted_list += left[left_index:]
                break
    return sorted_list

# test cases
a = [12, 11, 13, 5, 6, 7]
b = [0,9,0,1]
c = [0]
d = [4,3,2,1]

print merge(a)
print merge(b)
print merge(c)
print merge(d)
