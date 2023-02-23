# import sys

# sys.stdin = open('input.txt')



def algo_gird(a):
    T = int(input())
    for test_case in range(1, T+1):
        # N : 컨테이너 수, M : 트럭 수
        N, M = list(map(int, input().split()))
        # w : 화물의 무게
        ws = list(map(int, input().split()))
        ws.sort()
        # t : 트럭의 중량
        ts = list(map(int, input().split()))
        ts.sort(reverse=True)
        total_weight = 0
        for t in ts:
            i = 0
            break_x = 0
            for j in range(len(ws)-1, -1, -1):
                if t >= ws[j] and break_x == 0:
                    w_current = ws.pop(j)
                    total_weight += w_current
                    break_x += 1
        print(f'#{test_case} {total_weight}')


print(algo_gird("""
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13
"""))