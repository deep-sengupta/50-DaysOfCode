let scrapeEmails = document.getElementById('scrapeEmails');
let saveEmails = document.getElementById('saveEmails');
let list = document.getElementById('emailList');
let scrapedEmails = [];

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    let emails = request.emails;
    scrapedEmails = emails || [];
    list.innerHTML = '';
    if (scrapedEmails.length === 0) {
        let li = document.createElement('li');
        li.innerText = "No emails found";
        list.appendChild(li);
    } else {
        scrapedEmails.forEach((email) => {
            let li = document.createElement('li');
            li.innerText = email;
            list.appendChild(li);
        });
    }
});

scrapeEmails.addEventListener("click", async () => {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: scrapeEmailsFromPage,
    });
});

saveEmails.addEventListener("click", () => {
    if (scrapedEmails.length === 0) {
        alert("No emails to save");
        return;
    }
    let blob = new Blob([scrapedEmails.join('\n')], { type: 'text/plain' });
    let url = URL.createObjectURL(blob);
    let a = document.createElement('a');
    a.href = url;
    a.download = 'emails.txt';
    a.click();
    URL.revokeObjectURL(url);
});

function scrapeEmailsFromPage() {
    const emailRegEx = /[\w\.=-]+@[\w\.-]+\.[\w]{2,3}/gim;
    let emails = [];
    function extractEmailsFromNode(node) {
        if (node.nodeType === Node.TEXT_NODE) {
            let foundEmails = node.textContent.match(emailRegEx);
            if (foundEmails) emails = emails.concat(foundEmails);
        } else if (node.nodeType === Node.ELEMENT_NODE) {
            for (let child of node.childNodes) {
                extractEmailsFromNode(child);
            }
        }
    }
    extractEmailsFromNode(document.body);
    chrome.runtime.sendMessage({ emails });
}
