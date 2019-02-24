# LOS2 - red dragon

문제를 보면 id에 길이 제한 걸려있고 no가 주어지는 데 pw를 알아와야한다.

id에는 최소한으로 쓰고 no에는 is_numeric을 만족하는 값만 넣어 pw를 블라인드로 빼와야 하는 거 같다.

is_numeric은 0x형식은 이해하지 못하고 앞에 개행, 공백, 탭 문자들이 있으면 무시하고 숫자인지를 판단한다.

이점을 이용해 마음대로 커스텀해서 클리어 해보겠다.

어떻게 하지 막혔다 어떻게 한글자식 자르지 않고 한글자식 검사가 가능할까........ ㅠ

MySQL은 별게 다 됬었다. 문자열 끼리 비교연산이 신기하게 되었었는데.. 한번 해보자

앞의 그린 드래곤 테이블로 했다

```sql
> select * from tt where email>'f';

+--------+--------------------+-------+
| id     | email              | score |
+--------+--------------------+-------+
| admin  | flag               |   200 |
| rubiya | rubiya805@gmail.cm |   100 |
+--------+--------------------+-------+

> select * from tt where email>'g';
+--------+--------------------+-------+
| id     | email              | score |
+--------+--------------------+-------+
| rubiya | rubiya805@gmail.cm |   100 |
+--------+--------------------+-------+
```

이 결과를 볼 때 > 와 같은 크기 대소 비교를 할 때에는 길이를 같게 RPAD를 맞춰주고 그것의 hex, binary 값의 크기를 비교하는 듯하다

```
0x666c6167 > 0x66000000
```

같이 말이다.

고로 크기 비교연산을 통해서 bf를 할 수 있겠다! (행복)

근데 대소문자중 소문자만 되서 바꾸니까 된다음...