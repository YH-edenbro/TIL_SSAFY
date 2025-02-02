import requests
import pprint

# 하드 코딩하는 변수는 대문자
URL = 'https://fakestoreapi.com/carts' # 요청 주소
# .get(URL) : URL 주소에 요청을 보내는 메서드

data = requests.get(URL)
print(data) 

# 출력결과: <Response [200]>
# [200]: 웹의 응답 코드 -> 정상적으로 응답하였습니다.
# [404]: 웹의 응답 코드 -> 그 주소는 찾을 수 없습니다.(알 수 없는 주소로 요청했다.)

# .json(): 데이터를 JSON 형태로 변환해주는 메서드
json_data = data.json()
print(json_data)

pprint.pprint(json_data)