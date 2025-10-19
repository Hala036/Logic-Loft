from collections import deque

# O(V + E)
def dfs(graph, s, visited=None):
    visited = set()
    parent = {node: None for node in graph}
    distance = {node: float('inf') for node in graph}
    distance[s] = 0
    order = []

    def dfs_visit(graph, s, visited):
        visited.add(s)
        order.append(s)
        for neighbor in graph[s]:
            if neighbor not in visited:
                parent[neighbor] = s
                distance[neighbor] = distance[s] + 1
                dfs_visit(graph, neighbor, visited)

    dfs_visit(graph, s, visited)

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
        "order": order,
        "result": res
    }    
