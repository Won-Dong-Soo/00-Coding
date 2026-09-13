def solution(edges):
    def find(node, p):
        tmp = p[node - 1]
        before = node
        while tmp != before:
            before = p[before - 1]
            tmp = p[before - 1]
        return tmp

    answer = [0,0,0,0]
    vertices = list(set([j for i in edges for j in i]))
    edge2 = [[] for _ in vertices]
    edge2.append([])
    edge3 = [[] for _ in vertices]
    edge3.append([])
    for edge in edges:
        edge2[edge[0]].append(edge[1])
        edge3[edge[1]].append(edge[0])

    other_sum = 0
    for vertex in vertices:
        if len(edge2[vertex]) >= 2 and len(edge3[vertex]) <= 0:
            answer[0] = vertex
            other_sum = len(edge2[vertex])
            break

    for i in range(len(edges)-1, -1, -1):
        if edges[i][0] == answer[0]:
            del edges[i]

    p = [i + 1 for i in range(len(vertices))]
    node = [i + 1 for i in range(len(vertices))]

    for i in range(len(edges)):
        edges[i] = list(edges[i])
        edges[i].sort()
        edges[i] = tuple(edges[i])

    for x in edges:
        pa = find(x[0], p)  # 1
        pb = find(x[1], p)  # 2
        if pa != pb:
            for i in range(len(p)):
                if p[i] == pb:
                    p[i] = pa
            p[x[1] - 1] = pa

    print(p)

    groups = [[] for _ in vertices]
    for i in range(len(vertices)):
        if i == answer[0]:
            continue
        groups[p[i]-1].append(i+1)

    print(groups)

    for group in groups:
        flag = True
        for node in group:
            if len(edge2[node]) == 2 and len(edge3[node]) == 2:
                flag = False
                answer[3] += 1
                break

            if len(edge2[node]) == 0 and len(edge3[node]) == 1:
                flag = False
                answer[2] += 1
                break

        if flag and group != []:
            answer[1] += 1

    return answer

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(edges))