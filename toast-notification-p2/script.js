let toastBox = document.getElementById("toastBox");
let successMsg = '<i class="fa-solid fa-circle-check"></i> Success: This is a success Toast';
let errorMsg = '<i class="fa-solid fa-circle-xmark"></i> Error: This is a error Toast';
let invalidMsg = '<i class="fa-solid fa-circle-exclamation"></i> Invalid: This is a invalid Toast';
let infoMsg = '<i class="fa-solid fa-circle-info"></i> Info: This is a info Toast';

function showToast(msg) {
    let toast = document.createElement("div");
    toast.classList.add("toast");
    toast.innerHTML = msg;
    toastBox.appendChild(toast);

    if (msg.includes('error')) {
        toast.classList.add("error")
    }

    if (msg.includes("invalid")) {
        toast.classList.add("invalid")
    }

    if (msg.includes("info")) {
        toast.classList.add("info")
    }

    setTimeout(() => {
        toast.remove();
    }, 5000)
}
