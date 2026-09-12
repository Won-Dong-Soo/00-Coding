com_N = int(input())
link_N = int(input())
link = []
for _ in range(link_N):
    link.append(tuple(map(int, input().split())))
    
visited = []
dq = []
st = 1
flag = False
while True:
    for x in link:
        if x[0] == st and x[1] not in visited+dq:
            dq.append(x[1])
        elif x[1] == st and x[0] not in visited+dq:
            dq.append(x[0])
    
    if st not in visited:
        visited.append(st)
    if dq == []:
        break
    st = dq[0]
    del dq[0]
print(len(visited)-1)
    
    
            
        