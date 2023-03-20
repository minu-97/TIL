import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(a_row,a_col):
    # 방문 여부
    visited = [[0] * N for _ in range(N)]
    # 방문 한 노드의 인덱스
    to_visits = deque()
    to_visits.append([a_row, a_col])
    # to_visits가 존재 할 때 까지 while문을 반복
    while to_visits:
        # to_visits에 저장됨 row,col값을 각각 저장한다.
        row, col = to_visits.popleft()
        # 전방위를 탐색할 것이므로 for문을 4번 반복하여 탐색한다.
        for idx in range(4):

            new_row = row + d_row[idx]
            new_col = col + d_col[idx]
            
            # if문의 조건 new_row,new_col 값이 각각 0이상 N미만 이고 maze[new_raw][new_col] 값이 1이 아닐 때 즉 벽이 아닐 때 그리고 방문한적이 없을 때
            if 0 <= new_row < N and 0 <= new_col < N and maze[new_row][new_col] != 1 and visited[new_row][new_col] == 0:
                # maze[new_row][new_col] 값이 0일때 이동 가능한 길
                if maze[new_row][new_col] == 0:
                    # 이때 방분여부를 표시하며 최단거리 계산을 위해서 현재 위해 있는 visited[row][col] 값에 + 1 을 해준다.
                    visited[new_row][new_col] = visited[row][col] + 1
                    # 방문한 노드 1로 초기화 해서 재방문 못하게 막음
                    maze[new_row][new_col] = 1
                    # print(visited)
                    # 새로운 노드와 컬럼 값을 to_visit에 저장해 준다.
                    to_visits.append([new_row, new_col])
                # maze[new_row][new_col] 값이 3일 때 도착지점임으로 
                # if 문안에서 return문을 실행해 준다.
                if maze[new_row][new_col] == 3:
                    # visited[row][col]값에 누적된 방문횟수를 return해준다
                    return visited[row][col]
    # 아무것도 리턴이 되지 않을 시 도달할 수 있는 방법이 없는 것이므로 0을 리턴해준다.
    return 0





T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 미로를 리스트를 통해서 만들어준다.
    maze = [list(map(int, input())) for _ in range(N)]
    # 4방위를 탐색할 수 있게 델타 탐색을 사용한다.
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]
    # 시작 노드를 찾기 위해 이중 포문을 사용하고 bfs 함수에 시작 노드를 넘긴다.
    for k in range(N):
        for j in range(N):
            if maze[k][j] == 2:
                f_r = k
                f_c = j

                print(f'#{tc} {bfs(f_r, f_c)}')



