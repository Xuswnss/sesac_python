const cells = document.querySelectorAll("button");
for (let cell of cells) {
  cell.onclick = () => {
    console.log("클릭한 버튼의 값 : " + cell.value);
  };
}
