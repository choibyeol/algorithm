# 음양 더하기 level 1
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# 소수 만들기 level 1
from itertools import combinations
import math

def solution(nums):
    answer = 0
    comb_nums = list(combinations(nums, 3))
    for num in comb_nums:
        if isPrime(sum(num)) == True:
            answer += 1
    return answer

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# 없는 숫자 더하기 level 1
def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            answer += i
    return answer

# 내적 level 1
def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            answer += i
    return answer

# 두 개 뽑아서 더하기 level 1
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            answer.append(numbers[i] + numbers[j])
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer

# 3진법 뒤집기 level 1
def solution(n):
    answer = ''
    while n != 0:
        answer += str(n % 3)
        n = int(n / 3)
    answer = int(answer)
    answer = str(answer)
    tmp = 1
    result = 0
    for i in range(len(answer)-1, -1, -1):
        result += int(answer[i]) * tmp
        tmp *= 3
    return result

# 로또의 최고 순위와 최저 순위 level 1
def solution(lottos, win_nums):
    answer = []
    lotto_dict = {2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    max_num, min_num = 0, 0
    for lotto in lottos:
        if lotto in win_nums:
            max_num += 1
            min_num += 1
        else:
            if lotto == 0:
                max_num += 1
    nums = [max_num, min_num]
    for num in nums:
        if num not in lotto_dict:
            answer.append(6)
        else:
            answer.append(lotto_dict[num])
    return answer

# 약수의 개수와 덧셈 level 1
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divisor(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

def divisor(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count

# 2016년 level 1
# 1, 3, 5, 7, 8, 10, 12 -> 31
# 2 -> 29
# 4, 6, 9, 11 -> 30
days_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
def solution(a, b):
    answer = ''
    temp = 0
    for i in range(1, a):
        temp += days_dict[i]
    temp += b
    answer = days[temp % 7]
    return answer

# 예산 level 1
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer

# 나머지가 1이 되는 수 찾기 level 1
def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
    return answer

# 부족한 금액 계산하기 level 1
def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += price * (i + 1)
    answer = money - answer
    if answer < 0:
        return abs(answer)
    else:
        return 0

# 나누어 떨어지는 숫자 배열 level 1
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if answer == []:
        answer.append(-1)
    answer.sort()
    return answer

# 두 정수 사이의 합 level 1
def solution(a, b):
    answer = 0
    if a == b:
        return a
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        answer += i
    return answer

# 멀쩡한 사각형 level 2
from math import gcd

def solution(w,h):
    answer = w * h - (w + h - gcd(w, h))
    return answer