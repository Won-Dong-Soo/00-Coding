import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
subtree = [1 for _ in range(N+1)]
parents = [0 for _ in range(N+1)]
for i in range(N-1):
    c, p = map(int, input().strip().split())
    parents[c] = p
    tree[p].append(c)
    
target = int(input())

########################
## DFS
########################
# def dfs(target = 1):
#     cnt = 1
#     for i in tree[target]:
#         cnt += dfs(i)
#     return cnt

# print(dfs(target))

########################
## Whole Node
########################
# def dfs(target):
#     for i in tree[target]:
#         dfs(i)
#         subtree[target] += subtree[i]
# dfs(1)
# print(subtree)

########################
## Distance to root
########################

# 1. using parents
# root_dist = 0
# pos = target
# while pos != 1:
#     root_dist += 1
#     pos = parents[pos]
# print(root_dist)

# 2. not using parents
# tree에서 각각의 부모 찾기. 

########################
##가장 먼 자손노드와의 거리
########################
mdepth = 0
print(tree)
def dfs(node, depth):
    global mdepth
    depth += 1
    for i in tree[node]:
        mdepth = max(dfs(i, depth)-1, mdepth)
    if node == target:
        return mdepth
    return depth
        
print(dfs(target, 0))


