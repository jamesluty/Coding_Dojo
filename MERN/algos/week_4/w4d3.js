/* 
 ██╗ ██╗ 
████████╗
╚██╔═██╔╝
████████╗
╚██╔═██╔╝
 ╚═╝ ╚═╝ 
         
    Given two :violin: strings S and T containing only lowercase letters and "#" characters,
    return if they are equal when both are typed into empty text editors.
    :point_right: '#' character means a 'backspace' character.
    i.e., after processing the backspaces, are the two strings equal?
    return true or false
    Ninja Bonus: solve in O(n) time
*/

// ad#clp
// aclp

//          v
const S1 = "ab#c";
// a -> ab -> a -> ac
//          v
const T1 = "ad#c";
// a -> ad -> a -> ac
const expected1 = true;
// Explanation: Both S and T become "ac"

//             v
const S2 = "ab##";
// ["a", "b"]
// "str1"
// a -> ab -> a -> ""

const T2 = "c#d#";
// []
// "str2"
// c -> "" -> d -> "" 
const expected2 = true;
// Explanation: Both S and T become ""

const S3 = "a##c";
// a -> "" -> "" -> c
const T3 = "#a#c";
// "" -> a -> "" -> c
const expected3 = true;
// Explanation: Both S and T become "c"

const S4 = "a#c";
// a -> "" -> c
const T4 = "b";
// b
const expected4 = false;
// Explanation: S becomes "c" while T becomes "b".


function backspaceStringCompare(S, T) {
    let outputStr1 = S;
    let outputStr2 = T;
    let i=1;
    while(i <= outputStr1.length){
        if (outputStr1[i] === "#"){
            if(i>0){
                outputStr1 = outputStr1.slice(0, i-1) + outputStr1.slice(i+1)
            } else {
                outputStr1 = outputStr1.slice(0, i) + outputStr1.slice(i)
            }
            i=0
        }
        i++
    }
    i=0
    while(i <= outputStr2.length){
        if (outputStr2[i] === "#"){
            if(i>0){
                outputStr2 = outputStr2.slice(0, i-1) + outputStr2.slice(i+1)
            } else {
                outputStr2 = outputStr2.slice(0, i) + outputStr2.slice(i)
            }
            i=0
        }
        i++
    }
    console.log(outputStr1)
    console.log(outputStr2)
    if(outputStr1 === outputStr2){
        return true
    }
    return false
}

console.log(backspaceStringCompare(S1, T1))
console.log(backspaceStringCompare(S2, T2))
console.log(backspaceStringCompare(S3, T3))
console.log(backspaceStringCompare(S4, T4))