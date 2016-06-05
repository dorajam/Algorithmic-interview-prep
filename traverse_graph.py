# June 2016

graph = [1,9,3,4,10,6]
stack = []
res = []

def DFS(graph, root):
    stack.push(root)
    while len(res) < len(graph):
        u = stack.pop()
        res.append(u)

        for node in get_adj(u):
            if node not in path:
                stack.push(node)
    return res
