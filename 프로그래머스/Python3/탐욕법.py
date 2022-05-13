# 체육복 - level 1
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    temp = []
    for res in reserve:
        if res in lost:
            temp.append(res)
    for num in temp:
        lost.remove(num)
        reserve.remove(num)
    # set 차집합 연산으로 처리하는 게 더 쉬움
    # set(lost) - set(reserve)
    # set(reserve) - set(lost)
    answer = n - len(lost)
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            answer += 1
            continue
        for j in reserve:
            if abs(i-j) <= 1:
                reserve.remove(j)
                answer += 1
                break

    return answer