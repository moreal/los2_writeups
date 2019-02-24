# LOS2 - assassin

```sql
select id from prob_assassin where pw like '{$_GET[pw]}'
```

쿼리가 위와 같이 생겼다. 그리고 '을 사용할 수 없으므로 저 안에서 탈출 할 수 없다.

이 문제에서는 like의 와일드 카드를 사용할 줄 아는 가를 묻는다 %와 _이다.

_로 문자 길이를 게싱하고 하나하나 대입하며 나머지를 겟한다.

다만 추가적인 sql 삽입이 어려워 느린 bsqli 밖에 답이 없는 듯핟... ㅠㅜㅜ