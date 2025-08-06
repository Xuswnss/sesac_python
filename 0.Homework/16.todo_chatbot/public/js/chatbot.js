document.addEventListener("DOMContentLoaded", initChatbot);

function initChatbot() {
  createChatbotUI();
  registerEventHandlers();
}

function createChatbotUI() {
  const chatbotHTML = `
       <div class='chatbot-icon' id='chatbotIcon'>
        <i class="bi bi-chat-dots-fill"></i>
     </div>

     <div class="chatbot-window" id="chatbotWindow" style="display:none">
        <div class="chatbot-header">
          <span>chatbot</span>
          <button id='closeChatbot'>x</button>
        </div>
        <div class="chatbot-body">
          <div class="chatbot-messages" id="chatbotMessages"></div>
          <div class="chatbot-input-container">
              <input type="text" id="chatbotInput" placeholder="Type a message..">
              <button id="sendMessage">send</button>
          </div>
        </div>
     </div>
    `;

  // ✅ Fix: Use insertAdjacentHTML instead of insertAdjacentElement
  document.body.insertAdjacentHTML("beforeend", chatbotHTML);
}

function registerEventHandlers() {
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
    chatbotIcon.style.display = "block"; // ✅ Fix: 다시 아이콘 보이게
  });

  sendMessage.addEventListener("click", handlerUserMessage);

  chatbotInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      handlerUserMessage();
    }
  });
}

async function handlerUserMessage() {
  const input = document.getElementById("chatbotInput");
  const message = input.value.trim(); // ✅ Fix: ariaValueMax → value
  if (!message) return;


    addMessage(message, 'user')
    input.value = ''
    const botResponse = await sendMessageToServer(message)
    addMessage(botResponse, 'bot')
}// end handlerUserMessage

function addMessage(message, sender) {
  const container = document.getElementById("chatbotMessages");

  const messageElement = document.createElement("div");
  messageElement.innerHTML =
    sender === "user"
      ? `<i class='bi bi-person'></i> ${message}`
      : `<i class='bi bi-robot'></i> ${message}`;

  messageElement.classList.add(sender);
  container.appendChild(messageElement);
  container.scrollTop = container.scrollHeight;
}

const ECHO_MODE = false;

async function sendMessageToServer(userInput){
    if (ECHO_MODE) {
        console.log('에코모드 실행중입니다.')
        return `ECHO : ${userInput}`
    }
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers : {'Content-Type' : 'application/json'},
        body: JSON.stringify({userInput})
    })
    const data = await response.json()
    console.log("#### sendMessageToServer" , data);
    return data.chatbot // 나중에 서버의 응답 변수로 변경해야함.
}// end sendMessageToServer()
