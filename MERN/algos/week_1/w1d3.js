/* 
    https://visualgo.net/en/sorting
    Selection sort works by iterating through the list, finding the minimum
    value, and moving it to the beginning of the list. Then, ignoring the first
    position, which is now sorted, iterate through the list again to find the
    next minimum value and move it to index 1. This continues until all values
    are sorted.
    Unstable sort.
    Time Complexity
        - Best: O(n^2) quadratic.
        - Average: O(n^2) quadratic.
        - Worst: O(n^2) quadratic.
    
    Space: O(1) constant.
    Selection sort is one of the slower sorts.
        - ideal for: pagination, where page 1 displays 10 records for example,
        you run selection sort for 10 iterations only to display the first 10
        sorted items...
*/

const myArr = [3,2,9,5,1,4,8]

function selectionSort(arr){
    let min; // declaring the min value to use later
    for (let i=0; i<arr.length; i++){ // first for loop to loop through all indexes
        min = i; // setting min value to index i in array
        for (let j=i+1; j<arr.length; j++){ // looping through array start one after i to compare index j with i
            if (arr[j] < arr[min]){ // comparing the value of index j with index min to determine lowest value
                min = j; // setting index min to index j
            }
        }
        // after j for loop completes we compare the value of index min with index i
        if (arr[min] < arr[i]){
            // swapping values of index positions
            let temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
    // returning the sorted array
    return arr;
}

console.log(selectionSort(myArr));