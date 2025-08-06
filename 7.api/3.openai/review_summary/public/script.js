async function submitReview() {
  const rating = document.querySelector('input[name="rating"]:checked');
  const opinion = document.getElementById("opinion").value;

  if (!rating || !opinion.trim()) {
    alert("평점 또는 후기 내용이 입력되지 않았습니다.");
    return;
  }

  const review = {
    rating: parseInt(rating.value),
    opinion,
  };

  const response = await fetch("/api/reviews", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(review),
  });
  const data = await response.json();
  console.log(data);

  // 내가 쓴 글 불러오기 및 AI요약 요청을 동시에 둘다 비동기
  fetchReviews();
  fetchAISummary();
}

async function fetchReviews() {
  // 이거 전체도 try catch 로 감싸야함 (모든 fetch)
  const response = await fetch("/api/reviews");
  if (!response.ok) {
    throw new Error("요청 오류");
  }
  const data = await response.json();
  reviews = data.reviews;
  console.log(reviews);
  displayReview(reviews);
}

function displayReview(reviews) {
  const reviewsContainer = document.getElementById("reviews-container");
  // 기존에 작성된 후기글들 지우고 새로 그리기
  reviewsContainer
    .querySelectorAll(".review-box")
    .forEach((box) => box.remove());

  reviews.forEach((review) => {
    const reviewRow = document.createElement("div");
    reviewRow.className = "review-box";
    reviewRow.innerHTML = `
            <p class="review-header">Rating: ${review.rating}</p>
            <p>${review.opinion}</p>
        `;
    reviewsContainer.appendChild(reviewRow);
  });
}

document.getElementById("languageSelect").addEventListener("change", () => {
  fetchAISummary(); // 언어 바뀔 때마다 AI 요약 다시 가져오기
});
async function fetchAISummary() {
  const lang = document.getElementById('languageSelect').value
  console.log('####### lang : ', lang)
  const response = await fetch(`/api/ai-summary?lang=${lang}`);
  // 오류처리 생략
  const data = await response.json();
  console.log("data.targetLang :", data.targetLang);
  // console.log(data);
  displayAISummary(data);
}

function displayAISummary(data) {
  const summaryBox = document.querySelector(".ai-summary");
  summaryBox.innerHTML = `
        <p><strong>AI 요약:</strong> ${data.summary}</p>
        <p><strong>평균 별점:</strong> ${data.averageRating.toFixed(2)}</p>
    `;
}

window.onload =  () => {
   fetchReviews();
   fetchAISummary();
};
