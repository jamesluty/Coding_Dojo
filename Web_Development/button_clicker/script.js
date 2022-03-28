function login(logState) {
    if (logState.innerText == "Login"){
        logState.innerText = "Logout";
    } else {
        logState.innerText = "Login";
    }
}

function remove(button) {
    button.remove();
}

function likes(like, update) {
    alert(like);
    update.innerText = "1 like"
}