# 🍜 여행 맛집 추천 웹서비스

> AI가 여행지에 딱 맞는 맛집을 추천해주는 웹 서비스입니다.
> 가고 싶은 지역과 취향을 입력하면, AI가 분석해 실제 존재하는 맛집을 추천해 드립니다.

🔗 **배포 URL (Live Demo)** :https://mission-a1-3-82ghdcv96-codyssey11.vercel.app/

---

## 📖 1. 서비스 소개

**여행 맛집 추천 서비스**는 처음 가보는 낯선 여행지에서
"뭘 먹어야 할지" 고민하는 사용자를 위해 만들어졌습니다.

사용자가 **여행 지역**과 **원하는 음식 취향(분위기/메뉴 등)**을 입력하면,
**Google Gemini AI**가 취향을 분석하고 **Kakao Local API**로 실제 존재하는
맛집 정보를 찾아 추천해 줍니다.

### 🎯 서비스 목적
- 여행지에서의 맛집 검색 시간을 줄이고, 선택의 고민을 덜어준다.
- 단순 검색이 아닌 **AI 기반 취향 맞춤 추천**으로 만족도를 높인다.

### 👥 타겟 사용자
- 처음 가는 여행지에서 맛집 정보가 부족한 여행객
- 많은 검색 결과 속에서 결정을 어려워하는 사용자
- 자신의 취향에 맞는 맞춤 추천을 원하는 사용자

---

## 🖥️ 2. 페이지 구성 (3개 이상 / 네비게이션 이동 가능)

| 페이지 | 파일 | 설명 |
|--------|------|------|
| 🏠 홈 | `index.html` | 서비스 소개 및 시작하기 버튼 (메인 랜딩 페이지) |
| 🔍 추천받기 | `recommend.html` | 지역/취향 입력 → AI 맛집 추천 결과 출력 (핵심 기능) |
| ℹ️ 소개 | `about.html` | 서비스 설명, 사용 방법, 기술 스택 안내 |

- 상단 **네비게이션 바(메뉴)**를 통해 모든 페이지로 자유롭게 이동 가능합니다.
- **반응형 디자인**으로 데스크톱 / 태블릿 / 모바일 모두 정상 표시됩니다.

---

## 🤖 3. AI 기능 명세 (입력 / 출력 / 실패 처리)

### ✅ 핵심 기능 : AI 맛집 추천
사용자 입력을 AI가 분석하여 맞춤형 맛집 리스트를 제공합니다.

| 구분 | 내용 |
|------|------|
| **입력 (Input)** | 여행 지역(예: 부산 해운대), 취향/키워드(예: 혼밥 가능한 조용한 국밥집) |
| **처리 (Process)** | Gemini AI가 취향 분석 → Kakao Local API로 실제 맛집 검색 → 결과 정리 |
| **출력 (Output)** | 추천 맛집 이름, 주소, 추천 이유, 카테고리 등을 카드 형태로 화면에 표시 |
| **제공 가치** | 검색 시간 절약 + 취향 맞춤 추천 + 실제 존재하는 신뢰도 높은 정보 |

### ⚠️ 실패 처리 기준
사용자 경험을 위해 아래 상황을 안내 메시지로 처리합니다.

- **빈 입력 (필수값 누락)** : "지역과 취향을 모두 입력해 주세요." 안내 메시지 출력
- **API 오류 (4xx/5xx)** : "추천을 가져오는 중 문제가 발생했어요. 잠시 후 다시 시도해 주세요." 안내
- **지연/로딩** : 요청 중 로딩 스피너(또는 "추천을 찾는 중..." 메시지) 표시로 대기 상태 안내

---

## 🛠️ 4. 기술 스택

### Frontend
- **HTML5** : 페이지 구조 설계
- **CSS3** : 스타일링 및 반응형 디자인 (미디어 쿼리)
- **JavaScript (Vanilla)** : 사용자 입력 처리, `fetch`로 API 호출, 결과 화면 렌더링

### Backend (Serverless)
- **Python** : Vercel Serverless Functions (`api/recommend.py`)
- **Google Gemini API** : 사용자 취향 분석 및 추천 생성
- **Kakao Local API** : 실제 맛집 위치/정보 검색

### 배포 & 형상관리
- **Vercel** : 서버리스 배포 및 자동 CI/CD
- **GitHub** : 소스 코드 관리 및 버전 관리

---

## 📂 5. 프로젝트 구조

```
codyssey_travel_web/
├── index.html           # 홈 페이지
├── recommend.html       # 추천받기 페이지
├── about.html           # 소개 페이지
├── css/
│   └── style.css        # 전체 스타일 및 반응형
├── js/
│   └── main.js          # 입력 처리 / fetch 요청 / 결과 렌더링
├── api/
│   └── recommend.py     # 백엔드 (Gemini + Kakao 연동)
├── images/              # 이미지 리소스
├── requirements.txt     # Python 패키지 목록
├── vercel.json          # Vercel 배포 설정
└── README.md            # 프로젝트 문서
```

> 📌 **프론트(HTML/CSS/JS)**와 **백엔드(api/)** 구조가 명확히 분리되어 있습니다.

---

## 🚀 6. 실행 방법 (로컬)

### 1) 저장소 클론
```bash
git clone https://github.com/본인아이디/저장소이름.git
cd 저장소이름
```

### 2) 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 3) Vercel CLI로 로컬 실행
```bash
# Vercel CLI 설치 (최초 1회)
npm install -g vercel

# 로컬 개발 서버 실행
vercel dev
```

> 💡 로컬에서 API 기능까지 테스트하려면 아래 **환경 변수 설정**이 필요합니다.
> 브라우저에서 `http://localhost:3000` 으로 접속하여 확인할 수 있습니다.

---

## 🔑 7. 환경 변수(API 키) 설정 방법

API 키는 **보안을 위해 코드에 직접 작성하지 않고 환경 변수로 관리**합니다.
(키가 노출되면 타인이 무단 사용해 요금이 부과되거나 계정이 정지될 수 있기 때문입니다.)

### 필요한 환경 변수
| 변수명 | 설명 |
|--------|------|
| `GEMINI_API_KEY` | Google Gemini API 키 |
| `KAKAO_API_KEY` | Kakao REST API 키 |

### ① 로컬 환경 설정 (`.env` 파일)
프로젝트 루트에 `.env` 파일을 만들고 아래와 같이 작성합니다.
```
GEMINI_API_KEY=여기에_본인_Gemini_키_입력
KAKAO_API_KEY=여기에_본인_Kakao_키_입력
```
> ⚠️ `.env` 파일은 반드시 `.gitignore`에 추가하여 GitHub에 올라가지 않게 합니다!

### ② 배포 환경 설정 (Vercel 대시보드)
1. Vercel 프로젝트 접속 → **Settings** 메뉴 클릭
2. **Environment Variables** 메뉴 선택
3. `GEMINI_API_KEY`, `KAKAO_API_KEY` 를 각각 **Key / Value**에 입력하고 저장
4. 저장 후 **Redeploy(재배포)** 하면 적용 완료!

---

## 🌐 8. 배포 방법 (Vercel)

1. GitHub 저장소에 코드를 Push 합니다.
   ```bash
   git add .
   git commit -m "커밋 메시지"
   git push
   ```
2. [Vercel](https://vercel.com) 접속 → **New Project** → 해당 GitHub 저장소 선택
3. 위 **7번**의 환경 변수를 등록합니다.
4. **Deploy** 버튼 클릭 → 배포 완료!
5. 이후 GitHub에 Push할 때마다 **자동으로 재배포**됩니다. (CI/CD)

---

## 🔄 9. 동작 흐름 (사용자 입력 → 결과 출력)

```
[사용자] 지역/취향 입력
      │
      ▼
[JavaScript] fetch('/api/recommend') 요청 전송
      │
      ▼
[Python Serverless] Gemini 분석 → Kakao 맛집 검색
      │
      ▼
[JavaScript] 응답(JSON) 수신 → 화면에 결과 카드 렌더링
      │
      ▼
[사용자] 추천 맛집 확인 ✅
```

---

## 📸 10. 증빙 자료

> 아래에 스크린샷 이미지를 첨부하세요. (`images/` 폴더에 저장 후 링크)

- 🖥️ **데스크톱 화면** : `![desktop](images/screenshot-desktop.png)`
- 📱 **모바일 화면** : `![mobile](images/screenshot-mobile.png)`
- 🤖 **AI 기능 동작 장면** : `![ai](images/screenshot-ai.png)`

---

## 📝 11. 회고 (배운 점)

- HTML(구조) / CSS(디자인) / JavaScript(동작)의 역할 분담을 이해했다.
- 사용자 입력이 `fetch` 요청으로 바뀌고 응답이 화면에 반영되는 흐름을 익혔다.
- Vercel Serverless Functions로 프론트에서 Python 백엔드를 호출하는 구조를 경험했다.
- API 키를 환경 변수로 안전하게 관리하는 이유를 이해했다.
- 로컬과 배포 환경의 차이를 알고, 수정 후 재배포하는 흐름을 익혔다.

---

**Made with ❤️ for Codyssey Mission A2**
