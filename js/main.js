// 1. HTML 요소 가져오기 (그대로 유지!)
const searchBtn = document.getElementById("searchBtn");
const regionInput = document.getElementById("region");
const resultBox = document.getElementById("result");

// ⭐️ async 추가! (API 기다릴 때 필요해)
searchBtn.addEventListener("click", async function () {

    // 3. 입력칸 값 가져오기 (그대로!)
    const region = regionInput.value;

    // 4. 빈칸 체크 (그대로!)
    if (region === "") {
        alert("지역을 입력해주세요! 😊");
        return;
    }

    // 7. 로딩 표시 (그대로!)
    resultBox.innerHTML = `<p>🔍 ${region}의 맛집을 찾는 중...</p>`;

    // ⭐️ 여기부터가 핵심! 진짜 백엔드 부르기!
    try {
        // 🌐 recommend.py에게 주문 넣기!
        const response = await fetch("/api/recommend", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ date: region })  // ← 입력값 보내기
        });

        // 📦 결과(JSON) 받기
        const data = await response.json();

        // 결과 영역 비우기
        resultBox.innerHTML = "";

        // 🃏 받은 데이터로 카드 만들기!
        data.forEach(function (place) {
            // 맛집 목록을 글자로 정리
            let restaurantList = "";
            place.restaurants.forEach(function (r) {
                restaurantList += `<li>🍴 ${r.name} <small>(${r.category})</small></li>`;
            });

            // 도시 카드 만들기
            const card = `
                <div class="place-card">
                    <h3>📍 ${place.city}</h3>
                    <p>${place.reason}</p>
                    <ul>${restaurantList}</ul>
                </div>
            `;
            resultBox.innerHTML += card;
        });

    } catch (error) {
        // ❌ 에러 나면 사용자에게 알려주기
        resultBox.innerHTML = `<p>😢 오류가 발생했어요. 다시 시도해주세요!</p>`;
        console.log("에러 내용:", error);  // 개발자용 확인
    }
});