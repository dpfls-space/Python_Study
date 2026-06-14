import urllib.request
import urllib.parse
import json

API = "https://api.open-meteo.com/v1/forecast"
# 매개변수를 url 인코딩 ---- (1)
values = {
    'latitude': 37.566,
    'longitude': 126.9784,
    "current": "temperature_2m,relative_humidity_2m,weather_code",
    "timezone": "Asia/Seoul"
}

params = urllib.parse.urlencode(values)

# 요청 전용 URL 생성 ---- (2)
url = API + "?" + params
print("요청 주소 = ", url)

# API 호출 및 JSON 데이터 읽기 ---- (3)
with urllib.request.urlopen(url) as response:
    json_data = json.load(response)

# 결과 출력 ---- (4)
print(json.dumps(json_data, ensure_ascii=False, indent=2))