const open = document.getElementById("open");

open.onclick = () => {
  showModal();
};

function showModal() {
  const modalWrapper = document.createElement("div");
  modalWrapper.className = "modal-wrapper";
  modalWrapper.innerHTML = ` 
      <div class="modal">
        <div class="modal-title">modal title</div>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi
          dolore repellendus tempora provident, ducimus iste? Quasi eligendi eos
          magni fugiat, exercitationem earum ad optio, deleniti ea cumque ipsam
          fugit vel.
        </p>
        <div class="close-wrapper">
          <button id="close">x</button>
        </div>
    </div>`;
  document.body.appendChild(modalWrapper);

  // js는 짧고 간결하게 짜려는 다양한 문법과 기법들이 있다.
  document.getElementById("close").onclick = () => {
    modalWrapper.remove();
  };
} // end showModal
