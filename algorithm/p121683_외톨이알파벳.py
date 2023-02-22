def solution(input_string):
    # 반환받을 빈문자열 생성
    answer =''
    count =1
    # 알파벳 정보를 받을 딕셔너리 생성
    check_dict = {}
    # 딕셔너리가 오류가 발생하지 않게
    # input_string[0]을 사용하여 초기화
    check_dict[input_string[0]] = []
    # check 리스트도 같은 방식으로 초기화
    check = [input_string[0]]
    # input_string에서 문자 하나씩 사용
    for txt in input_string:
        # check[-1]에 txt가 중복되지 않을시
        if txt not in check[-1]:
            # check 리스트에 txt추가
            check.append(txt)
            # check_dict에 키값 txt로 []값으로 같는 딕셔너리 생성
            check_dict[txt] = []
    
    ### 위의 코드 실행시 연속으로 중복되는 문자열을 제외시킨다

    print(check)

    for txt in check:
        # 전처리된 check 리스트에서 txt를 이용해 키값을 받음
        check_dict[txt].append(count)
        # 해당 키값의 value인 리스트에 1을 append한다
        
        # 위에서 입력 받은 check_dict의 해당 value리스트의 길이가 2이상일 때를
        # 외톨이 알파벳이라고 정의한다.
    for key in dict.keys():
        if len(dict[key]) >= 2:
            answer += key
    print(check_dict)
    # answer에 저장된 문자열은 중복이 있을 수 있으므로 set을 통해서 중복을 제거하고
    # sorted()를 통해서 정렬한뒤
    # "".join을 을통해서 하나의 문자열로 만든다.
    answer = "".join(sorted(set(answer)))
    # answer가 존재할 시 return answer
    if answer:
        return answer
    # 존재하지 않을 시 return 'N'
    else:
        return "N"
    
print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution('string'))
print(solution('zbzbz'))

