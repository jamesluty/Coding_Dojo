/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;


// are the strings the same length?

// create a function with two input parameters
// first, make both strings lowercase
// see if two lowercase strings are equal to one another
    // if they're the same, we return true
    // if they're not the same, return false


/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.
 */

function caseInsensitiveStringCompare(strA, strB) {
    firstString = strA.toLowerCase()
    secondString = strB.toLowerCase()
    if (firstString == secondString){
        console.log("true")
        return true
    } else {
        console.log("false")
        return false
    }
}

caseInsensitiveStringCompare(strA1, strB1)
caseInsensitiveStringCompare(strA2, strB2)
caseInsensitiveStringCompare(strA3, strB3)