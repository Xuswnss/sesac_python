document.addEventListener("DOMContentLoaded", () => {
  const chatContainer = document.getElementById("chat-container");
  const userInputForm = document.getElementById("user-input-form");
  const userInputField = document.getElementById("user-input");
  const loadingIndicator = document.getElementById("loading-indicator");

  userInputForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const userInput = userInputField.value;
    userInputField.value = ""; // 사용자 입력 초기화

    appendMessage("user", userInput);
    showLoadingIndicator();
    scrollToBottom();

    const chatGPTResponse = await getChatGPTResponse(userInput);

    hideLoadingIndicator();
    appendMessage("chatbot", chatGPTResponse);
    scrollToBottom();
  });

  function scrollToBottom() {
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }

  function showLoadingIndicator() {
    loadingIndicator.style.display = "flex";
  }

  function hideLoadingIndicator() {
    loadingIndicator.style.display = "none";
  }

  function appendMessage(role, content) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", role);
    messageDiv.textContent = content;
    chatContainer.appendChild(messageDiv);
  }

  async function getChatGPTResponse(userInput) {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userInput }),
    });

    const data = await response.json();
    console.log(data);

    // 응답 받아서 반환
    return data.response;
  }
});
