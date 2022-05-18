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