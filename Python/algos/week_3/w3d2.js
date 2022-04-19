/* 
  Given two arrays, interleave them into one new array.
  The arrays may be different lengths. The extra items should be added to the
  back of the new array.
*/

const two_arrA1 = [1, 2, 3];
const two_arrB1 = ["a", "b", "c"];
const two_expected1 = [1, "a", 2, "b", 3, "c"];

const two_arrA2 = [1, 3];
const two_arrB2 = [2, 4, 6, 8];
const two_expected2 = [1, 2, 3, 4, 6, 8];

const two_arrA3 = [1, 3, 5, 7];
const two_arrB3 = [2, 4];
const two_expected3 = [1, 2, 3, 4, 5, 7];

const two_arrA4 = [];
const two_arrB4 = [42, 0, 6];
const two_expected4 = [42, 0, 6];

/**
 * Interleaves two arrays into a new array. Interleaving means alternating
 * the items starting from the first array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr1
 * @param {Array<any>} arr2
 * @returns {Array<any>} A new array of interleaved items.
 */

function interleaveArrays(arr1, arr2) {
    let output = [];
    let maxLength = 0;
    if (arr1.length == arr2.length){
        maxLength = arr1.length
    } else if (arr1.length < arr2.length) {
        maxLength = arr2.length
    } else {
        maxLength = arr1.length
    }
    for (let i = 0; i < maxLength; i++){
        if (i < arr1.length){
            output.push(arr1[i]);
        }
        if (i < arr2.length){
            output.push(arr2[i]);
        }
    }
    return output
}

// console.log(interleaveArrays(two_arrA1, two_arrB1))
// console.log(interleaveArrays(two_arrA2, two_arrB2))
// console.log(interleaveArrays(two_arrA3, two_arrB3))
// console.log(interleaveArrays(two_arrA4, two_arrB4))

/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */

function binarySearch(sortedNums, searchNum) {
    let left = 0;
    let right = sortedNums.length-1;

    while (left <= right){
        let mid = Math.floor((right + left) / 2);

        if (sortedNums[mid] == searchNum){
            return true
        }

        if (searchNum < sortedNums[mid]){
            right = mid - 1
        } else {
            left = mid + 1
        }

    }

    return false
}

console.log(binarySearch(nums1, searchNum1))
console.log(binarySearch(nums2, searchNum2))
console.log(binarySearch(nums3, searchNum3))
console.log(binarySearch(nums4, searchNum4))