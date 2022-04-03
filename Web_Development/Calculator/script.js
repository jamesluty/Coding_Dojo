var displayDiv = document.querySelector('#display');
var equation = "";

function press(numInput){    
    var number = "";
    if(displayDiv.innerText == 0){
        equation = numInput;
        displayDiv.innerText = numInput;
    } else {
        displayDiv.innerText += numInput;
        number += numInput;
        equation += number;
    }
}

function setOP(math){
    equation += math;
    displayDiv.innerText = equation;
}

function clr(){
    displayDiv.innerText = 0;
    equation = "";
}

function calculate(){
    var answer = eval(equation);
    displayDiv.innerText = answer;
}