chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "start") {
        chrome.declarativeNetRequest.updateEnabledRulesets(
            { enableRulesetIds: ["ruleset_1"] }
        );
    } else if (message.action === "stop") {
        chrome.declarativeNetRequest.updateEnabledRulesets(
            { disableRulesetIds: ["ruleset_1"] }
        );
    }
});
