const wrapper = document.querySelector(".wrapper"),
toast = wrapper.querySelector(".toast"),
title = toast.querySelector("span"),
subTitle = toast.querySelector("p"),
wifiIcon = toast.querySelector(".icon"),
closeIcon = toast.querySelector(".close-icon");

let isOnline = null;

window.onload = () => {
    function ajax() {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", "https://jsonplaceholder.typicode.com/posts", true);
        xhr.onload = () => {
            if (xhr.status == 200 && xhr.status < 300) {
                if (isOnline === false || isOnline === null) {
                    showOnlineToast();
                    isOnline = true;
                }
            } else {
                if (isOnline === true || isOnline === null) {
                    showOfflineToast();
                    isOnline = false;
                }
            }
        };
        xhr.onerror = () => {
            if (isOnline === true || isOnline === null) {
                showOfflineToast();
                isOnline = false;
            }
        };
        xhr.send();
    }

    function showOnlineToast() {
        wrapper.classList.remove("hide");
        toast.classList.remove("offline");
        title.innerText = "You're online now";
        subTitle.innerText = "Hurray! Internet is connected";
        wifiIcon.innerHTML = '<i class="uil uil-wifi"></i>';
        closeIcon.onclick = () => {
            wrapper.classList.add("hide");
        };
        setTimeout(() => {
            wrapper.classList.add("hide");
        }, 5000);
    }

    function showOfflineToast() {
        wrapper.classList.remove("hide");
        toast.classList.add("offline");
        title.innerText = "You're offline now";
        subTitle.innerText = "Oops! Internet is disconnected";
        wifiIcon.innerHTML = '<i class="uil uil-wifi-slash"></i>';
        closeIcon.onclick = () => {
            wrapper.classList.add("hide");
        };
        setTimeout(() => {
            wrapper.classList.add("hide");
        }, 5000);
    }

    setInterval(() => {
        ajax();
    }, 1000);
};