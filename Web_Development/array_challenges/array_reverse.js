function reverse(arr) {
    var revArr = []

    for(var i=arr.length-1; i>=0; i--){
        revArr.push(arr[i]);
    }
    arr = revArr;

    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]
