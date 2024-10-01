const word = document.getElementById("word");
const text = document.getElementById("text");
const scoreElement = document.getElementById("score");
const highScoreElement = document.getElementById("high-score");
const timeElement = document.getElementById("time");
const endgameElement = document.getElementById("end-game-container");
const startButton = document.getElementById("start-button");

let randomWord;
let score = 0;
let time = 30;
let highScore = localStorage.getItem("highScore") || 0;
highScoreElement.innerText = highScore;

let timeInterval;
let gameStarted = false;

async function getRandomWord(){
    const response = await fetch('https://random-word-api.herokuapp.com/word');
    const data = await response.json();
    return data[0];
}

async function addWordToDom(){
    randomWord = await getRandomWord();
    word.innerText = randomWord;
    if(!gameStarted){
        timeInterval = setInterval(updateTime, 1000);
        gameStarted = true;
    }
}

function updateScore(){
    score++;
    scoreElement.innerText = score;
}

function updateTime(){
    time--;
    timeElement.innerText = time + "s";
    if(time === 0){
        clearInterval(timeInterval);
        gameOver();
    }
}

function gameOver(){
    if(score > highScore){
        highScore = score;
        localStorage.setItem("highScore", highScore);
        highScoreElement.innerText = highScore;
    }

    endgameElement.innerHTML = `
        <h1>Time ran out</h1>
        <p>Your final score is ${score}</p><br>
        <button onclick="history.go(0)">Play Again</button>
        `;
    endgameElement.style.display = "flex";
}

startButton.addEventListener("click", () => {
    text.disabled = false;
    text.style.width = "100%";
    text.focus();
    startButton.style.display = 'none';
    addWordToDom();
});

text.addEventListener("input", async (e) => {
    const insertedText = e.target.value;
    if(insertedText === randomWord){
        e.target.value = "";
        await addWordToDom();
        updateScore();
        time += 3;
        updateTime();
    }
});