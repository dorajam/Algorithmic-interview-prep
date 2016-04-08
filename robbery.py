# rob houeses with max total value -> houses cant be adjecent

houses = [1,2,5,4,3,2,7]
houses.sort()
print type(houses)
d = {houses[i]:i for i in range(len(houses))}
print d

def rob(a):
    first = a[0]
    i=0
    val=0
    for i in range(len(a)-2):
        if d.get(a[i],0) - 1 == d.get(a[i+1]) or d.get(a[i],0) + 1 == d.get(a[i+1]):
            robbed = a[i]
            val += robbed
            if d.get(robbed,0) - 1 == d.get(a[i+1]) or d.get(robbed,0) + 1 == d.get(a[i+1]):
                if d.get(robbed, 0) - 1 == d.get(a[i+2]) or d.get(robbed,0) +1 == d.get(a[i+2]):
                    i += 3
                else:
                    i += 2


print rob(houses)
