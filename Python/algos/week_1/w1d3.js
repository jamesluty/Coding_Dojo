/* 
    Given in an alumni interview in 2021.
    String Encode
    You are given a string that may contain sequences of consecutive characters.
    Create a function to shorten a string by including the character,
    then the number of times it appears. 


    If final result is not shorter (such as "bb" => "b2" ),
    return the original string.

    pseudocode
    - create a function that takes in a string
    - 

  */

const str1 = "aaaabbcdddaaa";
const expected1 = "a4b2c1d3a3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function convertString(str){
    let strArray = str.split("")
    let newString = ""
    let count = 1
    for (i=0; i<strArray.length; i++) {
        if (strArray.length < 2){
            newString = str
        } else if (strArray[i] == strArray[i+1]){
            count += 1
        } else {
            newString += strArray[i] + count
            count = 1
        }
    }
    if (newString.length >= str.length){
        console.log(str)
        return str
    } else {
        console.log(newString)
        return newString
    }
}

// convertString(str1)
// convertString(str2)
// convertString(str3)
// convertString(str4)

    /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
    function encodeStr(str) {}

//   *********************************************

/* 
    String Decode  
*/

const two_str1 = "a3b2c1d3";
const two_expected1 = "aaabbcddd";

const two_str2 = "a3b2c12d10";
const two_expected2 = "aaabbccccccccccccdddddddddd";

function decodeStr(str){
    let decoded = ""
    let numStr = ""
    let letter = str[0]
    
    for (let i = 1; i < str.length; i++){
        let num = parseInt(str[i])

        if (isNaN(num)){
            let repeatStr = myRepeat(letter, numStr)
            decoded += repeatStr
            letter = str[i]
            numStr = ""
        } else {
            let whileNum = i
            while (!isNaN(str[whileNum])){
                numStr =+ str[whileNum]
                whileNum++
            }
            numStr = num
        }
    }
    console.log(decoded)
}

function myRepeat(letter, num){
    let output = ""
    for (let i=0; i<num; i++){
        output += letter
    }
}

decodeStr(two_str1)
decodeStr(two_str2)


/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
// function decodeStr(str) {}