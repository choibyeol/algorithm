# k번째수
def solution(array, commands):
    answer = []
    list = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1];
        idx = commands[i][2] - 1;
        list = array[start:end]
        list.sort()
        answer.append(list[idx])
    return answer