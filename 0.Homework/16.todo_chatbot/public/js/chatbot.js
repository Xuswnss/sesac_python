document.addEventListener("DOMContentLoaded", initChatbot);

function initChatbot() {
  createChatbotUI();
  registerEventHanders();
}

function createChatbotUI() {
  const chatbotHTML = `
        <div class="chatbot-icon" id="chatbotIcon">
            <i class="bi bi-chat-dots-fill"></i>
        </div>

        <div class="chatbot-window" id="chatbotWindow">
            <div class="chatbot-header">
                <span>Chatbot</span>
                <button id="closeChatbot">X</button>
            </div>
            <div class="chatbot-body">
                <div class="chatbot-messages" id="chatbotMessages"></div>
                <div class="chatbot-input-container">
                    <input type="text" id="chatbotInput" placeholder="Type a message...">
                    <button id="sendMessage">Send</button>
                </div>
            </div>
        </div>
    `;
  document.body.insertAdjacentHTML("beforeend", chatbotHTML);
}

function registerEventHanders() {
  const chatbotIcon = document.getElementById("chatbotIcon");
  const chatbotWindow = document.getElementById("chatbotWindow");
  const closeChatbot = document.getElementById("closeChatbot");
  const sendMessage = document.getElementById("sendMessage");
  const chatbotInput = document.getElementById("chatbotInput");

  chatbotIcon.addEventListener("click", () => {
    chatbotIcon.style.display = "none";
    chatbotWindow.style.display = "flex";
  });

  closeChatbot.addEventListener("click", () => {
    chatbotWindow.style.display = "none";
    chatbotIcon.style.display = "flex";
  });

  sendMessage.addEventListener("click", handleUserMessage);
  chatbotInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") handleUserMessage();
  });
}

async function handleUserMessage() {
  const input = document.getElementById("chatbotInput");
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, "user");
  input.value = "";

  const botResponse = await sendMessageToServer(message);
  addMessage(botResponse, "bot");
}

function addMessage(message, sender) {
  const container = document.getElementById("chatbotMessages");

  const messageElement = document.createElement("div");
  messageElement.innerHTML =
    sender === "user"
      ? `<i class="bi bi-person"></i> ${message}`
      : `<i class="bi bi-robot"></i> ${addLine(message)}`;
  messageElement.classList.add(sender);

  container.appendChild(messageElement);
  container.scrollTop = container.scrollHeight;
}

function addLine(message) {
  return message.replace(/\n/g, "<br>");
}

const ECHO_MODE = false;

async function sendMessageToServer(userInput) {
  if (ECHO_MODE) {
    return `Echo: ${userInput}`;
  }

  const response = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ userInput }),
  });

  const data = await response.json();
  console.log("서버응답:", data);
  loadTodos();

  return data.chatbot; // 나중에 서버의 응답 변수로 변경해야함.
}
