# 📦 필요한 도구들 모두 맨 위에!
import os
import json
import requests
import google.generativeai as genai
from http.server import BaseHTTPRequestHandler  # Vercel이 쓰는 웹 서버 도구

# 🔑 비밀 키 꺼내기 (Vercel에서는 환경변수로 자동 설정됨)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")


# 🤖 Gemini에게 여행지 추천받기 (A1이랑 거의 똑같아!)
def get_travel_recommendations(travel_date):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-3.8-Flash")  # ⭐ 모델 이름 수정!

    prompt = f"""
    너는 여행 전문가야. {travel_date}에 여행하기 좋은 국내 여행지 3곳을 추천해줘.
    반드시 아래 JSON 형식으로만 답변해. 다른 설명은 절대 쓰지 마.
    {{
      "recommendations": [
        {{ "city": "도시 이름", "reason": "추천 이유 (한 문장)" }}
      ]
    }}
    """
    response = model.generate_content(prompt)
    return response.text


# 📋 Gemini 답변(글자)을 진짜 데이터로 바꾸기 (A1이랑 똑같아!)
def parse_recommendations(raw_text):
    text = raw_text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
    data = json.loads(text)
    return data["recommendations"]


# 🍜 카카오맵에서 맛집 검색 (A1이랑 똑같아!)
def search_restaurants(city):
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": f"{city} 맛집", "size": 5}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data["documents"]


# 🌐 ⭐️ 여기가 웹용의 핵심! 브라우저 요청을 처리하는 부분
class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. 웹페이지에서 보낸 데이터 받기
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        request_data = json.loads(body)
        travel_date = request_data.get("date")  # 날짜 꺼내기

        # 2. A1 함수들 그대로 활용!
        raw_result = get_travel_recommendations(travel_date)
        recommendations = parse_recommendations(raw_result)

        # 3. 각 도시마다 맛집 정보 추가하기
        result = []
        for place in recommendations:
            city = place["city"]
            restaurants = search_restaurants(city)
            # 맛집 이름이랑 카테고리만 뽑아서 정리
            food_list = [
                {"name": r["place_name"], "category": r["category_name"]}
                for r in restaurants
            ]
            result.append({
                "city": city,
                "reason": place["reason"],
                "restaurants": food_list
            })

        # 4. ⭐️ 결과를 JSON으로 웹페이지에 돌려주기!
        self.send_response(200)  # 200 = "성공!" 신호
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(result, ensure_ascii=False).encode("utf-8"))
