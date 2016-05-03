# Code Dojo
# May 2016

ls = [70,4,5,3,8,7,4,8,9,1,2,5,7,11,13,32,4,2,40,3,2,2,0,2,5,23]
# buy one, sell one -> maximize your profit

def maxprofit(ls):
    min_num = ls[0]
    max_num = ls[0]
    max_dif = 0
    for i in range(len(ls)):
        max_dif = max_num - min_num 
        if ls[i] > max_num:
            max_num = ls[i]
        if ls[i] < min_num:
            if (max_num-min_num) > max_dif:
                max_dif = max_num - min_num
            min_num = ls[i]
            max_num = ls[i]
    return max_dif

# print maxprofit([1,2,3,2])

# def twoSells(ls):
#     min_num = ls[0]
#     max_num = ls[0]
#     max_dif = min_num - max_num
#     diffs = []
#     indeces = []

#     for i in range(len(ls)):
#         if ls[i] > max_num:
#             max_num = ls[i]
#             indeces.append(i)
#         if ls[i] < min_num:
#             max_dif.append(max_num - min_num)
#             min_num = ls[i]
#             max_num = ls[i]
#             max_index = i
#         if max_dif > diffs[-1]:
#             diffs.pop(0)
#             diffs.append(max_dif)

#     return max_num - min_num

print maxprofit(ls)

# def secondBest()
