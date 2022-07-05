# 신고 결과 받기 level 1 (왜 level 1일까...)
def solution(id_list, report, k):
    answer = []
    id_dic = {}
    report_dic = {}
    # id_dic, report_dic 초기화
    for i in range(len(report)):
        new_report = report[i].split()
        id_dic[new_report[0]] = []
        report_dic[new_report[1]] = 0
        
    # id_dic 신고 내역 추가
    for i in range(len(report)):
        new_report = report[i].split()
        id_dic[new_report[0]].append(new_report[1])
        
    # 같은 유저가 여러 번 신고한 것 -> set으로 하나만 취급
    # report_dic에 신고 당한 횟수 저장
    for key in id_dic.keys():
        id_dic[key] = set(id_dic[key])
        new_report = id_dic[key]
        for report in new_report:
            report_dic[report] += 1
    
    for i in range(len(id_list)):
        key = id_list[i]
        answer.append(0)
        if key not in id_dic.keys():
            continue
        for report in id_dic[key]:
            if report_dic[report] >= k:
                answer[i] += 1

    return answer

# [1차] 뉴스 클러스터링 level 2
def solution(str1, str2):
    answer = 0
    str1_list = []
    str2_list = []
    for i in range(len(str1)-1):
        string = str1[i] + str1[i+1]
        string = string.lower()
        if string.isalpha() == False:
            continue
        else:
            str1_list.append(string)
                
    for i in range(len(str2)-1):
        string = str2[i] + str2[i+1]
        string = string.lower()
        if string.isalpha() == False:
            continue
        else:
            str2_list.append(string)

    # 다중집합 확장
    str1_temp = str1_list.copy()
    union = str1_list + str2_list
    intersection = []
    for i in str2_list:
        if i in str1_temp:
            str1_temp.remove(i)
            intersection.append(i)
    inter_temp = intersection.copy()
    for i in inter_temp:
        if i in union:
            union.remove(i)
    if intersection == [] and union == []:
        answer = 1
    else:
        answer = len(intersection) / len(union)
    answer = int(answer * 65536)
    # set으로 하면 다중집합 체크 안됨
    # str1_set = set(str1_list)
    # str2_set = set(str2_list)
    # print(str1_set & str2_set, str1_set | str2_set)
    # if str1_set == set() and str2_set == set():
    #     answer = 1
    # else:
    #     answer = len(str1_set & str2_set) / len(str1_set | str2_set)
    return answer