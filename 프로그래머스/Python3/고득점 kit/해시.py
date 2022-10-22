# 폰켓몬 level 1
def solution(nums):
    if len(set(nums)) >= len(nums) / 2:
        return int(len(nums) / 2)
    else:
        return len(set(nums))

# 완주하지 못한 선수 level 1
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append('0')
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer

# 전화번호 목록 level 2
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(0, len(phone_book) - 1):
        if (phone_book[i] == phone_book[i+1][:len(phone_book[i])]):
            answer = False
            break
    return answer

# 위장 level 2
def solution(clothes):
    answer = 1
    comb = {}
    for element in clothes:
        key = element[1]
        if key in comb:
            comb[key] += 1
        else:
            comb[key] = 1
            
    for key in comb:
        answer *= comb[key] + 1
            
    return answer - 1

# 베스트앨범 level 3
import operator

def solution(genres, plays):
    answer = []
    genre_dic = {}
    play_dic = {}
    cnt = 0
    for genre in genres:
        genre_dic[genre] = 0
        play_dic[genre] = []
        
    for genre in genres:
        genre_dic[genre] += plays[cnt]
        play_dic[genre].append([cnt, plays[cnt]])
        cnt += 1
    
    genre_max = sorted(genre_dic.items(), key=operator.itemgetter(1), reverse=True)
    for genre in genre_max:
        play_max = []
        print(genre[0])
        for i in range(len(play_dic[genre[0]])):
            play_max.append([play_dic[genre[0]][i][1], play_dic[genre[0]][i][0]])
        play_max = sorted(play_max, key = lambda x : (-x[0], x[1]))
        for i in range(len(play_max)):
            answer.append(play_max[i][1])
            if i == 1:
                break
    
    return answer

# 베스트앨범 다른 풀이
def solution(genres, plays):
    answer = []
    genre = {}
    for i, g in enumerate(genres):
        if g not in genre:
            genre[g] = [plays[i], [i, plays[i]]]
        else:
            genre[g][0] += plays[i]
            genre[g].append([i, plays[i]])
    genre = dict(sorted(genre.items(), key = lambda x: (-x[1][0])))
    value = list(genre.values())
    for i in range(len(value)):
        tmp = sorted(value[i][1:], key = lambda x: -x[1])
        cnt = 0
        while cnt != 2:
            answer.append(tmp[cnt][0])
            if len(tmp) == 1:
                break
            cnt += 1
    
    return answer