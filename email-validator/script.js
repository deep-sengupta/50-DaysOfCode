validateBtn.addEventListener("click", async (e) => {
    e.preventDefault();
    console.log("Validate button clicked!");
    outputResult.innerHTML = `<img width="123" src="img/loading.svg" alt="Loading...">`;
    let apiKey = "YOUR API KEY";
    let email = document.getElementById("emailInput").value;
    let apiUrl = `https://api.emailvalidation.io/v1/info?apikey=${apiKey}&email=${email}`;
    let response = await fetch(apiUrl);
    let validationResult = await response.json();
    let displayString = ``;

    for(key of Object.keys(validationResult)){
        if (validationResult[key] !== "" && validationResult[key] !== " ") {
            displayString += `<div>${key}: ${validationResult[key]}</div>`;
        }
    }

    console.log(displayString);
    outputResult.innerHTML = displayString;
});