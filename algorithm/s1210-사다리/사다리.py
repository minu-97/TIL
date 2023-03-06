import sys
sys.stdin = open('input.txt')

# 사다리문제는 시작지점부터 끝지점을 찾아가는 것보다 명시된 끝지점에서 시작지점을 역으로 찾아가는 것이 편하다
# 이제부터 끝지점을 시작지점이라고 칭하겠다.
for test_case in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # # 델타 탐색
    d_rows = [0, 1, 0, -1]
    d_cols = [1, 0, -1, 0]
    idx = 1
    # 초기화
    # 시작 지점 찾기
    end_row = 99
    end_col = ladder[99].index(2)

    temp_col = end_col
    
    # 좌측 끝과 우측끝부터 경우의수를 시작하여 발생할 수있는 경우의 수를 최소화하였다
    # 그 뒤의 경우의 수는 시작 지점이 사다리 가운데에서 시작을 해 양쪽에 0이 있을 경우로 생각을하고 코드를 작성했다.
    while end_row > 0:
        if end_col == 0:
            if ladder[end_row][end_col+1] == 1:
                ladder[end_row][end_col] = 0
                end_col += 1
            else:
                ladder[end_row][end_col] = 0
                end_row -= 1
        if end_col == 99:
            if ladder[end_row][end_col-1] == 1:
                ladder[end_row][end_col] = 0
                end_col -= 1
            else:
                ladder[end_row][end_col] = 0
                end_row -= 1
        else:
            if ladder[end_row][end_col + 1] == 1:
                ladder[end_row][end_col] = 0
                end_col += 1

            elif ladder[end_row][end_col - 1] == 1:
                ladder[end_row][end_col] = 0
                end_col -= 1

            else:
                ladder[end_row][end_col] = 0
                end_row -= 1
    print(f'#{test_case} {end_col}')