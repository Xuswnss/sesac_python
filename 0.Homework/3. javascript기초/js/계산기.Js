const cells = document.querySelectorAll("button");
const inputContainer = document.getElementById("input-container");

// # input창에 값 추가하기
function addInput(value) {
  inputContainer.value += value;
  console.log("input Number : " + value);
} // end addInput()

// #계산
function calResult() {
  const vaild = /^[0-9+\-*/.\s]+$/;
  if (!vaild.test(inputContainer.value)) {
    alert("올바른 수식을 입력해주세요");
    inputContainer.value = "";
    console.log("올바른 식 입력");
    return;
  }
  const result = eval(inputContainer.value);
  inputContainer.value = result;
  console.log("계산 결과 : " + result);
} // end calResult

// # 초기화
function clearInput() {
  inputContainer.value = "";
  console.log("clearInput()");
} // end clearInput()

//버튼 순회해서 객체 뽑기
for (let cell of cells) {
  cell.onclick = () => {
    const cellValue = cell.value;
    console.log("클릭한 버튼 : " + cellValue);

    switch (cellValue) {
      case "=":
        calResult();
        break;
      case "c":
      case "C":
        clearInput();
        break;
      default:
        addInput(cellValue);
        break;
    }
  };
}

// enter 누르면 계산
inputContainer.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    calResult();
  }
});
