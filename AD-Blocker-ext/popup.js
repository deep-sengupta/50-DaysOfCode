document.getElementById('startbtn').addEventListener('click', () => {
    chrome.runtime.sendMessage({action: "start"});
});

document.getElementById('stopbtn').addEventListener('click', () => {
    chrome.runtime.sendMessage({action: "stop"});
});