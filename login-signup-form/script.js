const authWrapper = document.querySelector(".auth-wrapper"),
    toggleVisibility = document.querySelectorAll(".toggle-visibility"),
    switchAuthLinks = document.querySelectorAll(".switch-auth");

toggleVisibility.forEach(icon => {
    icon.addEventListener("click", () => {
        let passwordFields = icon.closest(".auth-field").querySelectorAll(".auth-password");

        passwordFields.forEach(password => {
            if (password.type === "password"){
                password.type = "text";
                icon.classList.replace("bx-hide", "bx-show");
                return;
            }
            password.type = "password";
            icon.classList.replace("bx-show", "bx-hide");
        });
    });
});

switchAuthLinks.forEach(link => {
    link.addEventListener("click", e => {
        e.preventDefault();
        authWrapper.classList.toggle("show-signup");
    });
});
