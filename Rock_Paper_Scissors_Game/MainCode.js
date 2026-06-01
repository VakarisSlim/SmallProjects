const pickingButton = document.getElementById('pickingButton');
const rockButton = document.getElementById('rockButton');
const paperButton = document.getElementById('paperButton');
const scissorsButton = document.getElementById('scissorsButton');
const para = document.getElementById('text');

function changePickingButtonText() {
        const options = {
        "Rock": "rock.png",
        "Paper": "paper.png",
        "Scissors": "scissors.png"
    };
    const randomChoice = Object.keys(options)[Math.floor(Math.random() * Object.keys(options).length)];
    document.getElementById("buttonImage").src = options[randomChoice];
    document.getElementById("buttonImage").alt = randomChoice; // Updates alt text for accessibility
    return randomChoice;
}

function changeText(choice){
    para.textContent = choice;
}

rockButton.addEventListener('click', function() {
    const choice = changePickingButtonText();
    if(choice == "Rock") {changeText("Draw")}
    else if(choice == "Paper") {changeText("You lose")}
    else if(choice == "Scissors") {changeText("You win")}
});

paperButton.addEventListener('click', function() {
    const choice = changePickingButtonText();
    if(choice == "Paper") {changeText("Draw")}
    else if(choice == "Scissors") {changeText("You lose")}
    else if(choice == "Rock") {changeText("You win")}
});

scissorsButton.addEventListener('click', function() {
    const choice = changePickingButtonText();
    if(choice == "Scissors") {changeText("Draw")}
    else if(choice == "Rock") {changeText("You lose")}
    else if(choice == "Paper") {changeText("You win")}
});