# 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append('0')
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer

# 전화번호 목록
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(0, len(phone_book) - 1):
        if (phone_book[i] == phone_book[i+1][:len(phone_book[i])]):
            answer = False
            break
    return answer

# 위장
def solution(clothes):
    answer = 1
    comb = {}
    for element in clothes:
        key = element[1]
        if key in comb:
            comb[key] += 1
        else:
            comb[key] = 1
            
    for key in comb:
        answer *= comb[key] + 1
            
    return answer - 1