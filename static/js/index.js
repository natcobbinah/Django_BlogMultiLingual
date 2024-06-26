
let fab_modal_btn = document.querySelector(".container-fluid .container .fab-container i")

let modal_view = new bootstrap.Modal('.container-fluid .staticBackdrop_modal')

fab_modal_btn.addEventListener('click', (event) => {
    console.log("clicked")
})

window.addEventListener('DOMContentLoaded', () => {
    modal_view.show()
})
