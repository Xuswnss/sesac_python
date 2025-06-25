const cells = document.querySelectorAll("button");
const inputContainer = document.getElementById("input-container");

/**
 *
 * 예외
 * 1. 0으로 나눌 수 없다
 * 2. symbol이 연속으로 나올 수 없다.
 * 3. 띄어쓰기를 없애기
 */

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
  // 나눗세밍 0인지 별도확인
  if (isDivisionByZero(inputContainer.value)) {
    inputContainer.value = "0으로 나눌 수 없습니다.";
  }

  try {
    const result = eval(inputContainer.value);
    inputContainer.value = result;
    console.log("계산 결과 : " + result);
  } catch (error) {
    console.log("발생한 오류 :" + error);
    inputContainer.value = "처리할 수 없습니다.";
  }
} // end calResult

function isDivisionByZero(expression) {
  for (let i = 0; i < expression.length; i++) {
    if (expression[i] === "/") {
      let current_position = i + 1;
      if (expression[current_position] === "0") {
        return true;
      }
    }
  }
} //end inDivision(expression)

// # 초기화
function clearInput() {
  inputContainer.value = "";
  console.log("clearInput() ; 초기화 되었습니다.");
} // end clearInput()

//버튼 순회해서 객체 뽑기
for (let cell of cells) {
  cell.onclick = () => {
    const cellValue = cell.value; //button의 value값 가져오기
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
