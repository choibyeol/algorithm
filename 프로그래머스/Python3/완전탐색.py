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

# 소수 찾기 level 2
import math
from itertools import permutations

def isPrime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        for num in list(permutations(numbers, i)):
            temp = ''
            for i in num:
                temp += i
            if isPrime(int(temp)) == True:
                answer.add(int(temp))
    cnt = len(answer)
    return cnt