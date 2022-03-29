function addLike(elem){
    var id = document.querySelector(elem);
    x = id.innerText.split(" ");
    var count = parseInt(x[0]);
    id.innerText = ++count + " like(s)"
}