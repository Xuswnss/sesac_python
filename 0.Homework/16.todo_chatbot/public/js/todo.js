// 미션1. /api/todo 에 CRUD 하기 추가
// GET /api/todo
// POST /api/todo
// PUT /api/todo/${id}
// DELETE /api/todo/${id}

document.addEventListener("DOMContentLoaded", () => {
  const todoForm = document.getElementById("todo-form");
  const textInput = document.getElementById("text-input");

  todoForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = textInput.value.trim();
    if (!text) return;
    textInput.value = ""; // 입력값 지우기

    // try catch 로 감싸서 예외처리해야함.
    // 여기는 퉁쳐서 두가지 다른 일을 하나로 잡았지만, 진짜 좋은 코드는 각각의 목적에 맞게 분리하는게 좋은거다. 하지만, "진짜 좋은" 의 정의가 무엇이냐?? 를 생각해 볼것...
    try {
      const response = await fetch("/api/todo", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      console.log(data);
    } catch (err) {
      console.error("백엔드 요청에 실패하였음: ", err);
    }

    loadTodos(); // 데이터 요청하기
  });

  // 최초 로딩 - 시작시 일단 현재 목록 불러오기
  loadTodos();
});

async function loadTodos() {
  const todoList = document.getElementById("todo-list");
  const res = await fetch("/api/todo");
  const data = await res.json();

  console.log(data);
  todoList.innerHTML = ""; // 현재 있는거 초기화
  data.forEach((task) => {
    const li = document.createElement("li");
    // 시큐어 코딩을 고려하면 이렇게 사용자의 입력값을 innerHTML로 뿌려주는 것은 매우 좋지 않은것임.
    // 좋은건?? 내가 DOM을 하나하나 그려서, 컨텐츠만 텍스트로 추가하게 하는게 좋은것임. (물론 짜기 매우 귀찮음)
    // 아니면 최소한의 방어책으로, 사용자 입력값은 검증한다.
    li.innerHTML = `
                <li class="list-group-item" style ="display : flex ; justify-content: space-between">

                <input  class="form-check-input " type="checkbox" ${
                  task.done ? "checked" : ""
                } onclick="toggleTodo(${task.id})">
                <span class="px-5" style="text-decoration: ${
                  task.done ? "line-through" : "none"
                }">${task.task}</span>
                <button class="btn btn-outline-danger" onclick="deleteTodo(${
                  task.id
                })">삭제</button>

                </li>

            `;
    todoList.appendChild(li);
  });
}

// 최소한의 방어책 - "입력값 검증을 한다"
function escapeHTML(str) {
  return String(str).replaceAll("<", "&lt;").replaceAll(">", "&gt;");
}

async function toggleTodo(id) {
  console.log('######## id',id)
  // 여기도 try catch 해야함.
  const response = await fetch(`/api/todo/${id}`, {
    method: "PUT",
  });
  const data = await response.json();
  console.log(data);
  loadTodos();
}

async function deleteTodo(id) {
  // 여기도 try catch 해야함.
  const response = await fetch(`/api/todo/${id}`, {
    method: "DELETE",
  });
  const data = await response.json();
  console.log(data);
  loadTodos();
}

// ul.innerHTML = `
//             <li class="list-group-item" style ="display : flex ; justify-content: space-between">
            
//             <input  class="form-check-input " type="checkbox" ${
//               item.done ? "checked" : ""
//             } onchange="toggleTodo(${item.id})">
//             <span class="px-5" style="text-decoration: ${
//               item.done ? "line-through" : "none"
//             }">${item.title}</span>
//             <button class="btn btn-outline-danger" onclick="deleteTodo(${
//               item.id
//             })">삭제</button>
            
//             </li>
           
            
//         `;
