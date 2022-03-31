function remove(acc, elem, conRequests, myConnections){
    var reqCount = document.querySelector(conRequests);
    var reqNum = reqCount.innerText;
    reqCount.innerText = reqNum -1;

    var conCount = document.querySelector(myConnections);
    var conNum = conCount.innerText;
    var newCount = parseInt(conNum[0] + conNum[1] + conNum[2]);
    
    if(acc){
        conCount.innerText = newCount + 1 + "+";
    }

    var user = document.querySelector(elem);
    user.remove();
}

function changeName(elem){
    var name = document.querySelector(elem);
    name.innerText = "Jamie Smith";
}