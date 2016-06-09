'''
# what's a set?
- {3,4,5,6}

# what's all subsets of a set?
{3,4,5}
{3}
{4,5}
{4}

# things to keep in mind:
- subsets of length n where n can be anyything in [0,len(set)]
- find all permutations of each subset, where the order doestn matter!
e.g. given {3,4} {4,3} -> same!
'''
import copy
def all_subsets(s):
    subs = [s]
    if len(s) < 1:
        return subs
    else:
        a = copy.copy(s)
        element = set([a.pop()])
        returned_subs = all_subsets(a)
        subs = returned_subs + [sub.union(element) for sub in all_subsets(a)]
    return subs

s = set([2,3,4,5])
print all_subsets(s)

# {} -> {}
# 2 -> {}, {2}

# 2,3 -> {}, {2}, {3}, {2,3}
# 2,3,4 -> {}, {2}, {3}, {4}, {2,3}, {2,4}, {3,4}, {2,3,4}
# difference:{4} {2,4}, {3,4}, {2,3,4}
# -> subs = func(n-1) + func(n-1) with new element in it
