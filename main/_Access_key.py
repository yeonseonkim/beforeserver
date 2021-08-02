import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'de161265f0532571bde6afea35f62760'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'JtwJwjRcINSsOiE7UMrkoLDCASJp-4cgdH965ZotF0rp4nS75L02zjEFd7oJsmsbOAibeAopcJ4AAAF68NTCGQ'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)