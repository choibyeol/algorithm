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

# 124 나라의 숫자 level 2
def solution(n):
    answer = ''
    nums = ['1', '2', '4']
    while n:
        n -= 1
        answer = nums[n % 3] + answer
        n //= 3
    return answer

# 문자열 내 p와 y의 개수 level 1
def solution(s):
    answer = True
    p_cnt, y_cnt = 0, 0
    for a in s:
        if a == 'p' or a == 'P':
            p_cnt += 1
        elif a == 'y' or a == 'Y':
            y_cnt += 1
    if p_cnt != y_cnt:
        answer = False
    return answer

# 문자열 내 마음대로 정렬하기 level 1
def solution(strings, n):
    answer = []
    answer = sorted(strings, key = lambda x:(x[n], x))
    return answer

# 문자열을 정수로 바꾸기 level 1
def solution(s):
    return int(s)

# 서울에서 김서방 찾기 level 1
def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 " + str(i) + "에 있다"
    return answer

# 약수의 합 level 1
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer

# 이상한 문자 만들기 level 1
def solution(s):
    answer = ''
    cnt = 0
    for i in range(len(s)):
        if cnt % 2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        cnt += 1
        if s[i] == ' ':
            cnt = 0
    return answer

# 자릿수 더하기 level 1
def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
    return answer

# 소수 찾기 level 1
def solution(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)

# 정수 내림차순으로 배치하기 level 1
def solution(n):
    answer = 0
    n = list(str(n))
    n.sort(reverse = True)
    answer = int(''.join(n))
    return answer

# 제일 작은 수 제거하기 level 1
def solution(arr):
    answer = []
    arr.remove(min(arr))
    if arr == []:
        answer.append(-1)
    else:
        answer = arr
    return answer

# 짝수와 홀수 level 1
def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"