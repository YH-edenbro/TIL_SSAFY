from collections import deque

def BFS(G, s, e):
    visited = [0] * (V+1)
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        t = q.popleft()
        if t == e:
            return visited[t] - 1

        for i in G[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1

    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        node, go = map(int, input().split())
        graph[node].append(go)
        graph[go].append(node)
    s, e = map(int, input().split())
    print(graph)
    result = BFS(graph, s, e)

    print(f"#{tc} {result}")