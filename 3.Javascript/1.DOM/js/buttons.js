console.log("start!!!");
let number = document.getElementById("result");

function number_int() {
  console.log("number_inc() active");
  number.textContent = Number(number.textContent) + 1;
  /*
  innerText - 글자만 가져온다 (디자인 속성을 적용받음)
  innerHTML - 글자와 태그까지 가져옴
  textContent - 순수 글자만 가져옴
  */

  let result = number_string_to_number + 1;
  number.textContent = result;
} // end number_int()

function number_dec() {
  console.log("number_dec( ) active");

  result.textContent = Number(result.textContent) - 1;
} // end number_dec()
