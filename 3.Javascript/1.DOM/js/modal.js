const open = document.getElementById("open");
const close = document.getElementById("close");
const modal = document.querySelector(".modal-wrapper");
// const modal = document.getElementsByClassName("modal-wrapper")[0];
// ⬆️ 위 내용은 'elements'이므로 이렇게 class를 가져오면 리스트로 가져오게 된다. 그러므로 index를 사용해 그 객체를 가져와야한다.
// 그러므로 객체가 하나만 존재할 떄는 아이디를 쓰거나 querySelector를 쓰는 것이 좋다.

// open.onclick = function openModal(){}
// open.onclick = function(){}
open.onclick = () => {
  modal.style.display = "flex";
};

close.onclick = () => {
  modal.style.display = "none";
};
