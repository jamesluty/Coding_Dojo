var add1 = document.querySelector("#likes1");
var add2 = document.querySelector("#likes2");
var add3 = document.querySelector("#likes3");
var count1 = 0
var count2 = 0
var count3 = 0

function addLike(){
    count1++
    add1.innerText = count1 + " like(s)"
}

function addLike2(){
    count2++
    add2.innerText = count2 + " like(s)"
}

function addLike3(){
    count3++
    add3.innerText = count3 + " like(s)"
}