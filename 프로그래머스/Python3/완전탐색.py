# 모의고사 level 1
def solution(answers):
    dic = {1: 0, 2: 0, 3: 0}
    len_answer = len(answers)
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    list_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    idx = 0
    for ans in answers:
        if ans == list_1[idx % 5]:
            dic[1] += 1
        if ans == list_2[idx % 8]:
            dic[2] += 1
        if ans == list_3[idx % 10]:
            dic[3] += 1
        idx += 1
    answer = []
    max_ans = max(dic[1], dic[2], dic[3])
    for num in dic.keys():
        if dic[num] == max_ans:
            answer.append(num)
    return answer