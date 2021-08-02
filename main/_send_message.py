import requests
import json

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)
# print(tokens)
# print(tokens["access_token"])

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

# GET /v1/api/talk/friends HTTP/1.1
# Host: kapi.kakao.com
# Authorization: Bearer {ACCESS_TOKEN}

headers={"Authorization" : "Bearer " + tokens["access_token"]}

result = json.loads(requests.get(friend_url, headers=headers).text)

friends_list = result.get("elements")

friend_id = friends_list[0].get("uuid")


send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"용기모아에서 구매하신 기프티콘입니다.",
        "link":{
            "web_url":"www.naver.com"
        },
        "button_title": "확인하러가기"
    })
}

response = requests.post(send_url, headers=headers, data=data)
response.status_code