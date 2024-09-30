const ratings = document.querySelectorAll(".rating");
const ratingsContainer = document.querySelector(".ratings-container");
const sendButton = document.getElementById("send");
const panel = document.getElementById("panel");
let selectedRating = "";

const removeActive = () => {
    ratings.forEach((rating) => rating.classList.remove("active"));
};

ratingsContainer.addEventListener("click", (e) => {
    if(e.target.closest(".rating")){
        removeActive();
        e.target.closest(".rating").classList.add("active");
        selectedRating = e.target.closest(".rating").getAttribute("data-value");
        sendButton.disabled = false;
    }
});

sendButton.addEventListener("click", () => {
    if(selectedRating){
        panel.innerHTML = `
            <div class="thank-you">
                <img src="https://gallery.yopriceville.com/var/albums/Animated-Gif-Images/Heart_GIF_Animation.gif" alt="Heart GIF" class="heart-gif">
                <strong>Thank you for your feedback!</strong>
                <br>
                <strong>Your rating: ${selectedRating}</strong>
                <p>Your input helps us improve our services. We appreciate your time and effort in sharing your thoughts with us.</p>
                <div class="beating-heart">
                    <i class="fas fa-heart heart-icon"></i>
                    <p>We value your feedback!</p>
                </div>
            </div>
        `;
    }
});