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

# 조이스틱 - level 2
'''
    # ord(문자) : 문자 -> 아스키코드
    # chr(숫자) : 숫자 -> 문자 변환

    print(ord('J') - ord('A')) # 9
    print(ord('E') - ord('A')) # 4
    print(ord('R') - ord('A')) # 17
    print(ord('O') - ord('A')) # 14
    print(ord('E') - ord('A')) # 4
    print(ord('N') - ord('A')) # 13
    9 + 4 + (26-17) + (26 - 14) + 4 + 13 + 5(이동 횟수)
'''
'''
# 정확도 74.1
def solution(name):
    answer = 0
    move = len(name) - 1
    while name[move] == 'A' and move > 0:
        move -= 1

    for i, alpha in enumerate(name):
        ascii = ord(alpha) - ord('A')
        answer += min(ascii, 26-ascii)
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        move = min(move, i + i + (len(name) - next))
        
    answer += move
    return answer
'''
# 정답 코드
def solution(name):
    if set(name) == {'A'}:
        return 0
    answer = float('inf') # 양의 무한대
    
    for i in range(len(name) // 2): # 반 이상 움직일 필요 X
        left_move = name[-i:] + name[:-i]
        right_move = name[i:] + name[:i]
        for n in [left_move, right_move[0] + right_move[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]
            row_move = i + len(n) - 1
            col_move = 0
            for alpha in map(ord, n):
                ascii = alpha - ord('A')
                col_move += min(ascii, 26 - ascii)

            answer = min(answer, row_move + col_move)
            
    return answer