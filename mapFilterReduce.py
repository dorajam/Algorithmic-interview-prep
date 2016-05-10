items = [1,2,3,4,5,6]
squared = []
for e in items:
    squared.append(e**2)

####################################
# define function and apply to each element

def sqr(x): return x**2
print list(map(sqr, items))

print list(map((lambda x: x **2), items))
