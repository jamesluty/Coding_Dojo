// given two sorted arrays that may have duplicate values, merge them and remove any duplicates
//          a
var arr1 = [1, 3, 3, 5, 8, 10,];
//          b
var arr2 = [1, 3, 3, 5, 8, 10, 10, 10];

var arrA = [1, 3, 4, 5];
var arrB = [1, 3, 3, 5, 8, 10];

function mergeDedupe(arr1, arr2) {
    let large;
    let small;
    let newArr = [];
    if (arr1.length > arr2.length){
        large = arr1;
        small = arr2;
    } else {
        large = arr2;
        small = arr1;
    }
    let i=0;
    let j=0;
    while (i < large.length && j < small.length){
        if (large[i] === small[j]){
            if (large[i] !== newArr[newArr.length-1]){
                newArr.push(large[i]);
                i++;
                j++;
            } else {
                i++;
            }
        } else if (large[i] < small[j]){
            if(large[i] !== newArr[newArr.length-1]){
                newArr.push(large[i])
                i++;
            } else {
                i++;
            }
        } else if (large[i] > small[j]){
            if(small[j] !== newArr[newArr.length-1]){
                newArr.push(small[j]);
                j++;
            } else {
                j++;
            }
        }
    }
    return newArr;
}

console.log(mergeDedupe(arr1, arr2))
console.log(mergeDedupe(arrA, arrB))

// try out some other tests
mergeDedupe([1, 3, 3, 5, 8, 10], [1, 3, 4, 5]) //expected: [ 1, 3, 4, 5, 8, 10 ]
mergeDedupe([2,3,3,5,8,10,12], [1,3,4,6]) //expected: [1, 2, 3, 4, 5, 6, 8, 10, 12]

// //   a -> 
//     [1, 3, 3, 5, 8, 10]
// //   b
//     [1, 3, 4, 5]