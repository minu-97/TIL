from collections import deque
import sys
sys.stdin = open('input.txt')

Node = int(input())
edge = int(input())
graph = [[] for _ in range(Node+1)]
visited = [[]for _ in range(Node+1)]

# 양방향 그래프 생성
for _ in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# dfs이용
def dfs(V):
    # 방문노드 표시
    visited[V] = True
    for new_v in graph[V]:
        if not visited[new_v]:
            dfs(new_v)
dfs(1)

# visited 노드에서 True값 카운트
# 처음 1번 노드가 필수적으로 True로 측정됨으로 -1을 해서 나머지 노드의 값을 구한다.
print(visited)
print(visited.count(True)-1)

visited_bfs = [[]for _ in range(Node+1)]

def bfs(V):
    to_visits = deque([V])
    while to_visits:
        # 현재 위치 = to_visits에서 popleft()
        current = to_visits.popleft()
        # print(current)
        # 현재 위치를 방문한 적이 없다면,
        if not visited_bfs[current]:
            # 현재 위치 방문 체크
            visited_bfs[current] = True
            to_visits += graph[current]

bfs(1)

print(visited_bfs.count(True)-1)
