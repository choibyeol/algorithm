// 완주하지 못한 선수
function solution(participant, completion) {
    participant.sort();
    completion.sort();
    for (let i in participant) {
        if (participant[i] != completion[i]) {
            return participant[i];
        }
    }
}

// 위장
function solution(clothes) {
    var answer = 1;
    var obj = {};
    for (var i = 0; i < clothes.length; i++) {
        obj[clothes[i][1]] = (obj[clothes[i][1]] || 1) + 1;
    }

    for (var key in obj) {
        answer *= obj[key];
    }

    return answer - 1;
}
