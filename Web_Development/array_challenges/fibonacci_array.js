function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    
    while(fibArr.length<n){
        var count = 0;
        for(var i=fibArr.length-2; i<fibArr.length; i++){
            count += fibArr[i];   
        }
        fibArr.push(count);
    }
    return fibArr;
}

var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
