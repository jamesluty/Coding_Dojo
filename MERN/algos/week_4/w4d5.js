// https://leetcode.com/problems/longest-substring-without-repeating-characters/

/* 
  Given a string, find the length of the longest substring without repeating characters.
*/
//                👇
const str1 = "abcabcbb";
const expected1 = 3;
// Explanation: The answer is "abc", with the length of 3.
//              v
const str2 = "bbbbb";
const expected2 = 1;
// Explanation: The answer is "b", with the length of 1.

const str3 = "pwwkew";
const expected3 = 3;
/* Explanation: The answer is "wke", with the length of 3. 
  Note that the answer must be a substring, "pwke" is a subsequence and not a substring. */
//              v
const str4 = "dvadf";
const expected4 = 4;
// Explanation: "vadf"


function lengthOfLongestSubString(str) {
    let tempStr = ""
    let count = 1;
    let maxCount = 0;
    for(let i=0; i<str.length; i++){
        tempStr += str[i]
        for(let j=i+1; j<str.length; j++){
            if(tempStr.includes(str[j])){
                tempStr = ""
                if(count > maxCount) {
                    maxCount = count
                }
                count = 1
                break;
            } else {
                tempStr += str[j]
                count++
            }
        }
    }
    return maxCount
}

console.log(lengthOfLongestSubString(str1))
console.log(lengthOfLongestSubString(str2))
console.log(lengthOfLongestSubString(str3))
console.log(lengthOfLongestSubString(str4))