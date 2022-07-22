# 비밀지도 level 1
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin1 = bin(arr1[i])
        bin2 = bin(arr2[i])
        sumstr = bin(int(bin1, 2) | int(bin2, 2))
        tmp = ''
        sumstr = sumstr[2:]
        for str in sumstr:
            if str == '1':
                tmp += '#'
            else:
                tmp += ' '
        if len(sumstr) < n:
            for i in range(n-len(sumstr)):
                tmp = ' ' + tmp
        answer.append(tmp)
    return answer

# [1차] 다트 게임 level 1
def solution(dartResult):
    bonus_dict = {'S': 1, 'D': 2, 'T': 3}
    answer = 0
    frontNum = 0
    num = ''
    isNums = True
    for dart in dartResult:
        if dart.isdigit() == True:
            if isNums == False:
                answer += num
                frontNum = num
            if isNums == True:
                num += dart
            else:
                num = dart
            isNums = True
        else:
            num = int(num)
            isNums = False
            if dart in bonus_dict:
                num = pow(num, bonus_dict[dart])
            else:
                if dart == '*':
                    num = num * 2
                    answer += frontNum
                elif dart == '#':
                    num = num * -1
    answer += num
    return answer