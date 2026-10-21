INF = float("inf")

def floyd_warshall_analysis(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    next_node = [[None] * n for _ in range(n)]
    
    # Initialize path reconstruction
    for i in range(n):
        for j in range(n):
            if graph[i][j] != INF:
                next_node[i][j] = j
                
    # Floyd-warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    candidate = dist[i][k] + dist[k][j]
                    
                    if candidate < dist[i][j]:
                        dist[i][j] = candidate
                        next_node[i][j] = next_node[i][k]
                        
    #  Find vertices belonginng to or affected by negative cycles
    negative_vertices = [
        k for k in range(n) if dist [k][k] < 0
    ]
    
    # Mark all pairs whose shortest paths are undefined
    undefind = [[False] * n  for _ in range(n)]
    
    for k in negative_vertices:
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    undefind[i][j] = True
                    
    return dist, next_node, negative_vertices, undefind

def reconstruct_path(next_node, start, end):
    if next_node[start][end] is None:
        return []
    
    path = [start]
    
    while start != end:
        start = next_node[start][end]
        path.append(start)
        
        if len(path) > len(next_node) + 1:
            return []
        
    return path

def display_result(dist, next_node, negative_vertices, undefined):
    n = len(dist)
    
    print("\nNEGATIVE CYCLE ANALYSIS")
    if negative_vertices:
        print("Negative cycle detected.")
        print("Affected cycle vertices:", negative_vertices)
    else:
        print("No negative-weight cycle detected.")
        
    print("\nALL-PAIRS SHORTEST PATH REPORT")
    
    for i in range(n):
        for j in range(n):
            if undefined[i][j]:
                print(f"{i} -> {j}: Undefined (negative cycle)")
            elif dist[i][j] == INF:
                print(f"{i} -> {j}: Unreachable")
            elif i == j:
                print(f"{i} -> {j}: Distance = 0, Path = {i}")
            else:
                path = reconstruct_path(next_node, i, j)
                route = " -> ".join(map(str, path))
                print(
                    f"{i} -> {j}: Distance = {dist[i][j]}, "
                    f"Path = {route}" 
                )
                
                
def main():
    graph = [
        [0,   4,   INF, INF, INF],
        [INF, 0,   -2,  INF, INF],
        [INF, -2,  0,   3,   INF],
        [INF, INF, INF, 0,   2],
        [1,   INF, INF, INF, 0]
    ]
    
    print("ADVANCED FLOYD-WARSHALL: NEGATIVE CYCLE ANALYSIS")
    print("Vertices:", len(graph))
    
    dist, next_node, negative_vertices, undefined = (
        floyd_warshall_analysis(graph)
    )
    
    display_result(
        dist, next_node, negative_vertices, undefined
    )
    
if __name__ == "__main__":
    main()
    
    