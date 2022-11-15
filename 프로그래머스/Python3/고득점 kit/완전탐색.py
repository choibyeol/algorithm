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

# 카펫 level 2
'''
bbbbbbbb
byyyyyyb
byyyyyyb
byyyyyyb
byyyyyyb
bbbbbbbb

bbbb
byyb
bbbb

사각형 위, 아래: (yellow의 약수 중 하나 + 2) * 2
yellow 양 옆: 2 * (yellow 총 개수 / 위에서 구한 약수)
두개를 더한 값이 brown이 되게
근데 가로가 세로보다 같거나 길어야 함.

가로: 사각형 위
세로: yellow 옆 + 2
'''

def division(num):
    div_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            div_list.append(i)
    return div_list

def solution(brown, yellow):
    answer = []
    div_list = division(yellow)
    for num in div_list:
        updown = (num + 2) * 2
        leftright = int(2 * (yellow / num))
        row = updown / 2
        col = leftright / 2 + 2
        if (updown + leftright) == brown and row >= col:
            break
    answer.append(row)
    answer.append(col)
    return answer

# 최소직사각형 level 1
def solution(sizes):
    maxs, mins = [], []
    for size in sizes:
        w, h = size[0], size[1]
        if w >= h:
            maxs.append(w)
            mins.append(h)
        else:
            maxs.append(h)
            mins.append(w)
    answer = max(maxs) * max(mins)
    return answer

# 모음사전 level 2
from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for w in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(w)))

    words.sort()
    return words.index(word) + 1