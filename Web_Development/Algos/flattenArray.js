// complete the following function
function flatten(arr2d) {
    var flat = [];

    for(i=0;i<arr2d.length; i++){
        var array = arr2d[i];
        console.log(array);

        for(x=0;x<array.length;x++){
            var innerArray = array[x];
            flat.push(innerArray);
        }
    }

    return flat;
}

var result = flatten( [ [2, 5, 8], [3, 6, 1], [5, 7, 7] ] );
console.log(result); // we expect to get back [2, 5, 8, 3, 6, 1, 5, 7, 7]
