def find(node, p):
    tmp = p[node-1]
    before = node
    while tmp != before:
        before = p[before-1]
        tmp = p[before-1]
    return tmp

# p = [1 2 1 4]
# node = [1 2 3 4]

com_N = int(input())
link_N = int(input())
link = []
for _ in range(link_N):
    link.append(tuple(map(int, input().split())))


p = [i + 1 for i in range(com_N)]
node = [i+1 for i in range(com_N)]
for i in range(len(link)):
    link[i] = list(link[i])
    link[i].sort()
    link[i] = tuple(link[i])

for x in link:
    pa = find(x[0], p)# 1
    pb = find(x[1], p)# 2
    if pa != pb:
        for i in range(len(p)):
            if p[i] == pb:
                p[i] = pa
        p[x[1]-1] = pa

cnt = 0
for i in range(com_N):
    if find(i, p) == find(1, p):
        cnt += 1
        
print(cnt)
#1 2 2 4