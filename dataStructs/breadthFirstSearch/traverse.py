# Dora Jambor
# bfs prob with strange messy input

# sample input
inp = [[2],
       [4,2],
       [1, 2],
       [1, 3],
       [1],
       [3, 1],
       [2, 3],
       [2]]

num_tests = inp[0]
num_nodes = inp[1][0]
num_edges = inp[1][1]
root = inp[4][0]

visited = [root]

connections = inp[2:4]
for i in range(len(connections)): 
    connections[i] = set(connections[i])

def get_neighbors(node):
    neighbors = []
    for e in connections:
        if node in e:
            (n,) = e - set([node])
            neighbors.append(n)
    if neighbors[0] in visited:
        return False 
    return neighbors


def isConnected(start,num):
    if set([start,num]) in connections:
        return True
    return False

def isLeaf(node):
    if not get_neighbors(node):
        return True
    return False

def shortest_path(root):
    total = 0
    if isLeaf(root):
        return 0
    
    neighbors = get_neighbors(root)

    for e in neighbors:
        if e not in visited:
            visited.append(e)
            # 6 units to visit
            total += 6

    for e in neighbors:
        total += shortest_path(e)
    return total

print shortest_path(root)
