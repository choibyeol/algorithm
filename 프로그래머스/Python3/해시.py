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
