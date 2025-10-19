import heapq

#O(V+E log V)
def dijkstra(graph, s):
    distance = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    H = [(0,s)]
    order = []
    distance[s] = 0

    while H:
        dist_u, u = heapq.heappop(H)
        if dist_u > distance[u]:
            continue
        order.append(u)
        for neighbor in graph[u]:
            v, d = neighbor
            dist_n = dist_u + d
            if dist_n < distance[v]:
                heapq.heappush(H, (dist_n, v))
                distance[v] = dist_n
                parent[v] = u

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
