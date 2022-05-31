let slideIdx = 0;

function changeImg(){
    let imgArray = ['slideShow1', 'slideShow2', 'slideShow3', 'slideShow4'];
    if(slideIdx === 0){
        document.getElementById(imgArray[3]).style.display = "none";
    }
    document.getElementById(imgArray[slideIdx]).style.display = 'inherit';
    if(slideIdx > 0){
        document.getElementById(imgArray[slideIdx-1]).style.display = "none";
    } 
    
    slideIdx++;
    if(slideIdx > imgArray.length-1){
        slideIdx = 0;
    }
    setTimeout(changeImg, 3000)
}

changeImg()

function highlight(navLink){
    navLink.style.background = "black";
}

function revert(navLink){
    navLink.style.background = "rgb(17,105,160)";
}