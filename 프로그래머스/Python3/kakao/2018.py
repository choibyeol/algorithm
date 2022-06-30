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