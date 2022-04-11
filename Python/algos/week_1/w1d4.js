/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

  const str1 = "a x a";
  const expected1 = true;
  
  const str2 = "racecar";
  const expected2 = true;
  
  const str3 = "Dud";
  const expected3 = false;
  
  const str4 = "oho!";
  const expected4 = false;

function isPalindrome(str){
    newStr = ""
    for (i=str.length-1; i>=0; i--){
        newStr += str[i]
    }
    if (newStr === str){
        console.log("String is a palindrome")
        return true
    } else {
        console.log("String is not a palindrome")
        return false
    }
}

// isPalindrome(str1)
// isPalindrome(str2)
// isPalindrome(str3)
// isPalindrome(str4)
  
  /**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */

//   ************************************

/* 
  Longest Palindrome
  For this challenge, we will look not only at the entire string provided,
  but also at the substrings within it.
  Return the longest palindromic substring. 
  Strings longer or shorter than complete words are OK.
  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
*/


const two_str1 = "what up, daddy-o?";
const two_expected1 = "dad";

const two_str2 = "uh, not much";
const two_expected2 = "u";

const two_str3 = "Yikes! my favorite racecar erupted!";
const two_expected3 = "e racecar e";

const two_str4 = "a1001x20002y5677765z";
const two_expected4 = "5677765";

const two_str5 = "a1001x20002y567765z";
const two_expected5 = "567765";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
function longestPalindromicSubstring(str) {
    let newStr = ""
    let tempStr = ""
    for (i=str.length-1; i>=0; i--){
        newStr += str[i]
    }
    tempCount = str.length -1
    for(x = 0; x < newStr.length; x++){
        tempCount -= 1
        if (newStr[x] == str[tempCount]){
            tempStr += newStr[x]
            console.log(tempStr)

            for ( y=str[tempCount]; y>0; y-- ){
                if (newStr[y] == str[y]){
                    console.log("test")
                    tempStr += newStr[y]
                    console.log(tempStr)
                }
            }
        } 
        
    }
}

longestPalindromicSubstring(two_str1)
// longestPalindromicSubstring(two_str2)
// longestPalindromicSubstring(two_str3)
// longestPalindromicSubstring(two_str4)
// longestPalindromicSubstring(two_str5)