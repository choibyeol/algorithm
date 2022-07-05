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

from itertools import combinations

# 메뉴 리뉴얼 level 2
def solution(orders, course):
    answer = []
    menu_dict = {}
    for order in orders:
        for i in course:
            if len(order) < i:
                continue
            comb = list(combinations(order, i))
            if i not in menu_dict:
                menu_dict[i] = {}
            for c in comb:
                menu = ''
                for j in range(len(c)):
                    menu += c[j]
                menu = ''.join(sorted(menu))
                if menu not in menu_dict[i]:
                    menu_dict[i][menu] = 1
                else:
                    menu_dict[i][menu] += 1

    for key in menu_dict.keys():
        menu_list = sorted(menu_dict[key].items(), key = lambda x : -x[1])
        value_menu = menu_list[0][1]
        for menu in menu_list:
            if menu[1] < 2:
                break
            if menu[1] != value_menu:
                break
            value_menu = menu[1]
            answer.append(menu[0])
    answer.sort()
    return answer