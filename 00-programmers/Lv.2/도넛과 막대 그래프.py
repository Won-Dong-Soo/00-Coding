def solution(edges):
    max_node = max(max(a, b) for a, b in edges)

    indegree = [0] * (max_node + 1)
    outdegree = [0] * (max_node + 1)

    for a, b in edges:
        outdegree[a] += 1
        indegree[b] += 1

    answer = [0, 0, 0, 0]

    for node in range(1, max_node + 1):
        # 생성 정점
        if indegree[node] == 0 and outdegree[node] >= 2:
            answer[0] = node

        # 막대 그래프
        elif outdegree[node] == 0 and indegree[node] >= 1:
            answer[2] += 1

        # 8자 그래프
        elif indegree[node] >= 2 and outdegree[node] >= 2:
            answer[3] += 1

    # 생성 정점에서 만들어진 그래프의 개수
    answer[1] = outdegree[answer[0]] - answer[2] - answer[3]

    return answer