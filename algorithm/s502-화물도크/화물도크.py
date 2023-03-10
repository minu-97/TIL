# 24시간 동안 A도크에서 최대 몇 대의 화물차가 이용 할 수 있는지
# A도크 사용신청서에 작업 시간과 완료시간이 매 정각을 기준으로 표시
# 앞 작업의 종료와 동시에 다음 작업 가능
import sys
sys.stdin = open('algorithm\s502-화물도크\input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    working_time = [list(map(int, input().split())) for _ in range(N)]
    working_time=sorted(working_time, key = lambda x: (x[1], x[0]))
    print(working_time)
    cnt = 0
    end = 0
    i = 0
    while i<len(working_time):
        if working_time[i][0] >= end:
            cnt += 1
            end = working_time[i][1]
        i+=1
    print(f'#{test_case} {cnt}')