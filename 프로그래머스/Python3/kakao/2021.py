# 신규 아이디 추천 level 1
def solution(new_id):
    answer = ''
    temp = ''
    special_list = ['-', '_', '.']
    
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for n in new_id:
        if n in special_list or n.isdigit() or n.isalpha():
            temp += n

    answer = temp
    temp = ''
    # 3단계
    check = 0
    for n in answer:
        if n == '.':
            check = 1
            continue
        else:
            if check == 1:
                temp += '.'
                temp += n
                check = 0
            else:
                temp += n        
    answer = temp
    # 4단계
    if answer[0:1] == '.':
        answer = answer[1:]
    if answer[-1:] == '.':
        answer = answer[:-1]
    # 5단계
    if answer == '':
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[0:15]
    while True:
        if answer[-1:] == '.':
            answer = answer[0:-1]
        else:
            break
    # 7단계
    if len(answer) <= 2:
        while True:
            if len(answer) >= 3:
                break
            else:
                answer += answer[-1:]
    
    return answer

# 숫자 문자열과 영단어 level 1
alpha = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def solution(s):
    answer = ''
    num = ''
    for i in s:
        if i.isdigit() == True:
            answer += i
        else:
            num += i
            if num in alpha:
                answer += alpha[num]
                num = ''
    answer = int(answer)
    return answer