function changeImg(){
    document.getElementById('slideShow1').style.display = 'none';
    
}

setTimeout(changeImg, 3000);

function highlight(navLink){
    navLink.style.background = "black";
}

function revert(navLink){
    navLink.style.background = "rgb(17,105,160)";
}