function changeImg(){
    var imgArray = ['slideShow1', 'slideShow2', 'slideShow 3', 'slideShow4'];
    for(i=0; i<imgArray.length; i++){
        document.getElementsByClassName(imgArray[i]).style.display = 'none';
        document.getElementsByClassName(imgArray[1]).style.display = 'inherit'
    }
}

setTimeout(changeImg, 3000);

function highlight(navLink){
    navLink.style.background = "black";
}

function revert(navLink){
    navLink.style.background = "rgb(17,105,160)";
}