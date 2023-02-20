def solution(gems):

    shelf = [i for i in gems]
    gems_set = {i for i in gems}
    shortest = []
    i = 0
    j = len(shelf)

    print(shelf)

    while i < len(shelf):
        for (shelf[i:])in gems_set:
            print(shelf[start:])
            if len(shelf[i:]) >= len(gems_set):
                i += 1
                print(len(shelf[i:]))
                while j < len(shelf):
                    for shelf[i:-j] in gems_set:
                        if len(shelf[i:j]) >= len(gems_set):
                            print(j)
                            print(shelf)
                            j -= 1
                    else:
                        print('len(shelf[i:-j]', len(shelf[i:j]))
                        break
        else:
            if i > len(shelf[i:-j]):
                shortest = (i, len(shelf[i:-j])+1)
            else:
                shortest = (i, len(shelf[i:-j])+i)
            break


    print(shortest)

    # return answer


print(solution(["DIA", "RUBY", "RUBY","DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
