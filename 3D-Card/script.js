const headphone = document.querySelector(".headphone img");
const sizeButtons = document.querySelectorAll(".size");

headphone.addEventListener("mouseenter", (e) => {
    headphone.style.transform = "rotateZ(-20deg) scale(1.1)";
});

headphone.addEventListener("mouseleave", (e) => {
    headphone.style.transform = "rotateZ(0deg) scale(1)";
});

sizeButtons.forEach(button => {
    button.addEventListener("click", () => {
        sizeButtons.forEach(btn => btn.classList.remove("active"));
        button.classList.add("active");
    });
});