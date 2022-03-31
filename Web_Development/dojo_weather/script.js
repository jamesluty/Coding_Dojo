function removeCookies(elem){
    var popup = document.querySelector(elem);
    console.log(popup);
    popup.remove();
}

function showAlert(){
    alert("Loading weather report...");
}

function changeTemp(degree,high1,high2,high3,high4,low1,low2,low3,low4){
    var changeDegree = degree.value;
    console.log(changeDegree);
    var newHigh1 = document.querySelector(high1);
    var newHigh2 = document.querySelector(high2);
    var newHigh3 = document.querySelector(high3);
    var newHigh4 = document.querySelector(high4);
    var newLow1 = document.querySelector(low1);
    var newLow2 = document.querySelector(low2);
    var newLow3 = document.querySelector(low3);
    var newlow4 = document.querySelector(low4);
    var parseHigh1 = parseInt(newHigh1.innerText);
    var parseHigh2 = parseInt(newHigh2.innerText);
    var parseHigh3 = parseInt(newHigh3.innerText);
    var parseHigh4 = parseInt(newHigh4.innerText);
    var parseLow1 = parseInt(newLow1.innerText);
    var parseLow2 = parseInt(newLow2.innerText);
    var parseLow3 = parseInt(newLow3.innerText);
    var parseLow4 = parseInt(newlow4.innerText);
    if (changeDegree == "fahrenheit"){
        newHigh1.innerText = "75°";
        newHigh2.innerText = "80°";
        newHigh3.innerText = "69°";
        newHigh4.innerText = "78°";
        newLow1.innerText = "65°";
        newLow2.innerText = "66°";
        newLow3.innerText = "61°";
        newlow4.innerText = "70°";
    } else {
        newHigh1.innerText = "24°";
        newHigh2.innerText = "27°";
        newHigh3.innerText = "21°";
        newHigh4.innerText = "26°";
        newLow1.innerText = "18°";
        newLow2.innerText = "19°";
        newLow3.innerText = "16°";
        newlow4.innerText = "21°";
    }
}
