import itertools


def solution(k, dungeons):
    answer = []
    #  itertools.permutations을 이용해 피로도와 상관없이 던전 이용의 모든 경우의 수 생성
    for i in itertools.permutations(dungeons,len(dungeons)):
        # 현재 피로도
        fatigue = k
        count = 0
        # 필요 피로도, 소모 피로도
        for essential, consume in i:
            # 필요 피로도가 현재 피로도 이하 일때
           if fatigue >= essential:
               # 현재 피로도에서 소모 피로도를 차감
               fatigue -= consume
               # count를 증가시켜서 던전 이용 기록
               count += 1
        answer.append(count)
   
    return max(answer)

print(solution(80,[[80,20],[50,40],[30,10]]))