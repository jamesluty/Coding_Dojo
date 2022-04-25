/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

const nums2 = [1];
const expected2 = 1;

const nums3 = [];
const expected3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */

function sumArr(nums, i=0) {
    // edge
    if ( nums.length == 0){
        return 0;
    }

    // base
    if ( i === nums.length - 1){
        return nums[i];
    }

    // recursive
    return nums[i] + sumArr(nums, ++i);
}

// console.log(sumArr(nums1))
// console.log(sumArr(nums2))
// console.log(sumArr(nums3))
// *************************************************************

/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const two_num1 = 5;
const two_expected1 = 15;
// Explanation: (1+2+3+4+5)

const two_num2 = 2.5;
const two_expected2 = 3;
// Explanation: (1+2)

const two_num3 = -1;
const two_expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
*/

function recursiveSigma(num) {
    // edge
    if ( num < 0){
        return 0;
    }
    num = Math.floor(num)

    // base
    if (num == 0) {
        return num
    }

    // recursive
    return num + recursiveSigma(--num)
}

console.log(recursiveSigma(two_num1))
console.log(recursiveSigma(two_num2))
console.log(recursiveSigma(two_num3))

