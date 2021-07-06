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

