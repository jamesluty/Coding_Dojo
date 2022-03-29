console.log("page loaded...");

var vid = document.getElementById("beach");

function start() {
    // console.log("over");
    vid.muted = true;
    vid.play();
}

function end() {
    // console.log("off");
    vid.pause();
}