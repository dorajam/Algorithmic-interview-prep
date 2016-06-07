# Dora Jambor
# June 2016

# Breadth first search
# Qs: is it a simple graph?

def get_adj(node):
    # return neighbors
    pass


def BFS(node):
    queue = [node]

    while len(queue) > 0:
        node = queue[0]
        for e in get_adj(node):
            if e not in path:
                queue.append(e)
        first_pop = queue.pop(0)
        path.append(first_pop)
    return path
