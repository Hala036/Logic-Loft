# O(V + E)
from collections import deque

def bfs(graph, s):
    color = {node: 'W' for node in graph}
    distance = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    color[s] = 'G'
    distance[s] = 0

    queue = deque([s])
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for n in graph[u]:
            if color[n] == 'W':
                color[n] = 'G'
                distance[n] = distance[u] + 1
                parent[n] = u
                queue.append(n)
        color[u] = 'B'

    res = {}
    for node in graph:
        if distance[node] == float('inf'):
            res[node] = {"distance": None, "path": None}
        else:
            path = []
            p = node
            while p is not None:
                path.insert(0, p)
                p = parent[p]
            res[node] = {"distance": distance[node], "path": path}

    return {
        "start": s,
        "order": order,
        "result": res
    }
