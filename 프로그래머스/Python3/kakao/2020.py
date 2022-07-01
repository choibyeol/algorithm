# 키패드 누르기 level 1
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
L_dict = {'i': 0, 'j': 0}
R_dict = {'i': 0, 'j': 0}
num_dict = {'i': 0, 'j': 0}

def solution(numbers, hand):
    answer = ''
    L_location = '*'
    R_location = '#'
    L_len = R_len = 0
    i = j = 0
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            L_location = num
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            R_location = num
        else:
            i = 0
            for keys in keypad:
                j = 0
                for key in keys:
                    j += 1
                    if key == L_location:
                        L_dict['i'] = i
                        L_dict['j'] = j
                    elif key == R_location:
                        R_dict['i'] = i
                        R_dict['j'] = j
                    if key == num:
                        num_dict['i'] = i
                        num_dict['j'] = j
                i += 1

            L_len = abs(num_dict['i'] - L_dict['i']) + abs(num_dict['j'] - L_dict['j'])
            R_len = abs(num_dict['i'] - R_dict['i']) + abs(num_dict['j'] - R_dict['j'])

            if L_len == R_len:
                if hand == 'right':
                    R_location = num
                    answer += 'R'
                else:
                    L_location = num
                    answer += 'L'
            else:
                if L_len > R_len:
                    R_location = num
                    answer += 'R'
                else:
                    L_location = num
                    answer += 'L'
                
    return answer

# 문자열 압축 level 2
def solution(s):
    answer = 0
    mins = len(s)
    tmpstr = s
    for i in range(1, int(len(s) / 2) + 1):
        num = 1
        tmpstr = ''
        tmp = s[0:i]
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                num += 1
            else:
                if num == 1:
                    tmpstr += tmp
                else:
                    tmpstr += str(num) + tmp
                    num = 1
            tmp = s[j:j+i]
        if num != 1:
            tmpstr += str(num) + tmp
        else:
            tmpstr += tmp
        if len(tmpstr) < mins:
            mins = len(tmpstr)
    answer = mins
    return answer

# 괄호 변환 level 2
def solution(p):
    answer = ''
    if p == '':
        return p
    if iscorrect(p):
        return p
    answer = rec(p)
    return answer

def divide(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            if i+1 < len(p):
                v = p[i+1:]
            else:
                v = ''
            break
    return u, v

def iscorrect(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def rec(p):
    result = ''
    tmp = ''
    if p == '':
        return p
    u, v = divide(p)
    if iscorrect(u):
        result = u + rec(v)
    else:
        tmp = '('
        tmp += rec(v)
        tmp += ')'
        u = u[1:-1]
        for c in u:
            if c == '(':
                tmp += ')'
            else:
                tmp += '('
    result += tmp
    return result