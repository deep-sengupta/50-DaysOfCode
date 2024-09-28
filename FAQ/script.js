const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach((faq, index) => {
    const header = faq.querySelector(".faq-header");
    const content = faq.querySelector(".faq-content");
    const icon = faq.querySelector(".faq-icon i");
    const iconContainer = faq.querySelector(".faq-icon");

    header.addEventListener("click", () => {
        const isOpen = content.style.height === `${content.scrollHeight}px`;

    faqItems.forEach((f, i) => {
        const c = f.querySelector(".faq-content");
        const ic = f.querySelector(".faq-icon i");
        const iconCont = f.querySelector(".faq-icon");

        if(i === index){
            c.style.height = isOpen ? "0px" : `${c.scrollHeight}px`;
            ic.classList.toggle("ri-add-line", isOpen);
            ic.classList.toggle("ri-subtract-fill", !isOpen);
            iconCont.classList.toggle("active", !isOpen);
            faq.classList.toggle("open", !isOpen);
        }else{
            c.style.height = "0px";
            ic.classList.remove("ri-subtract-fill");
            ic.classList.add("ri-add-line");
            iconCont.classList.remove("active");
            f.classList.remove("open");
        }
    });
    });
});