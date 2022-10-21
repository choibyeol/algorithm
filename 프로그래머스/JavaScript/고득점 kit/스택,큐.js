// 기능개발 level 2
function solution(progresses, speeds) {
  const answer = [];
  let time = 0;
  let cnt = 0;

  while (progresses.length > 0) {
    if (progresses[0] + time * speeds[0] >= 100) {
      progresses.shift();
      speeds.shift();
      cnt += 1;
    } else {
      if (cnt > 0) {
        answer.push(cnt);
        cnt = 0;
      }
      time += 1;
    }
  }
  answer.push(cnt);
  return answer;
}

// 올바른 괄호 level 2
function solution(s) {
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] == "(") stack.push(s[i]);
    else {
      if (stack.length == 0) return false;
      else stack.pop();
    }
  }
  if (stack.length != 0) return false;
  return true;
}
