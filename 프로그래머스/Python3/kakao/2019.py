# 크레인 인형뽑기 게임 level 1
def solution(board, moves):
    answer = 0
    doll = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                doll.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(doll) >= 2:
            if doll[-1] == doll[-2]:
                doll = doll[0:-2]
                answer += 2
    return answer

# 실패율 level 1
def solution(N, stages):
    answer = []
    f_rate = {}
    S = len(stages)
    for stage in range(1, N+1):
        if S != 0:
            count = stages.count(stage)
            f_rate[stage] = count / S
            S -= count
        else:
            f_rate[stage] = 0
    answer = sorted(f_rate, key = lambda x: f_rate[x], reverse=True)
    return answer

''' 처음 틀린 풀이
def solution(N, stages):
    answer = []
    stage_dict = {}
    f_rate = {}
    for stage in stages:
        if stage in stage_dict:
            stage_dict[stage] += 1
        else:
            if stage == N + 1:
                continue
            stage_dict[stage] = 1
            f_rate[stage] = 0
        
    P = len(stages)
    for i in range(1, N+1):
        if i in stage_dict:
            if i-1 in stage_dict:
                P -= stage_dict[i-1]
                f_rate[i] = stage_dict[i] / P
            else:
                f_rate[i] = stage_dict[i] / P
                
    for item in sorted(f_rate.items(), key = lambda x : (-x[1], x[0])):
        answer.append(item[0])
    for i in range(1, N+1):
        if i not in answer:
            answer.append(i)
    return answer
'''

# 오픈채팅방 level 2
def solution(record):
    answer = []
    user_dict = {}
    chats = []
    for i in range(len(record)):
        user_info = record[i].split()
        chat = user_info[0]
        user_id = user_info[1]
        if len(user_info) > 2:
            user_name = user_info[2]
            user_dict[user_id] = user_name
        if chat != 'Change':
            chats.append([chat, user_id])
            
    for chat in chats:
        id = chat[1]
        name = user_dict[id]
        if chat[0] == 'Enter':
            string = name + "님이 들어왔습니다."
            answer.append(string)
        elif chat[0] == 'Leave':
            string = name + "님이 나갔습니다."
            answer.append(string)
    return answer