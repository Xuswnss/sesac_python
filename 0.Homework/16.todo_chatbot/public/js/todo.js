window.onload = function () {
  fetchTodo()
  const form = document.getElementById("todo-form");
  form.addEventListener("submit", addTodo);
  console.log("페이지가 모두 로드되었습니다.");
};

async function fetchTodo() {
  const response = await fetch("/api/todo");
  const data = await response.json();
  const result = document.getElementById("todo-list");

  result.innerHTML = ""; 

  if (!data || data.length === 0) {
    result.innerHTML = `<p>일정을 추가해주세요</p>`;
    return;
  }

  data.forEach((item) => {
    const li = document.createElement("li");
    li.className = "todo-item";

    li.innerHTML = `
            <input type="checkbox" ${
              item.done ? "checked" : ""
            } onchange="toggleTodo(${item.id})">
            <span style="text-decoration: ${
              item.done ? "line-through" : "none"
            }">${item.title}</span>
            <button onclick="deleteTodo(${item.id})">삭제</button>
        `;

    result.appendChild(li);
  });
} // end fetchTodo()

async function addTodo(event) {
  event.preventDefault(); // 폼의 기본 동작(페이지 새로고침) 방지

  const input = document.getElementById("text-input");
  const title = input.value.trim();

  if (!title) {
    alert("할 일을 입력해주세요!");
    return;
  }

  const response = await fetch("/api/todo", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title }),
  });

  if (response.ok) {
    input.value = ""; 
    fetchTodo();
  } else {
    alert("추가에 실패했습니다.");
  }
}// end addTodo

async function toggleTodo(id) {
  await fetch(`/api/todo/${id}`, {
    method: "PUT",
  })
  fetchTodo(); 
}// end toggleTodo

async function deleteTodo(id) {
  await fetch(`/api/todo/${id}`, {
    method: "DELETE",
  });
  fetchTodo(); 
}// end deleteTodo




