import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    c, p = map(int, input().strip().split())
    graph[p].append(c)
    graph[c].append(p)
    
target = int(input())

