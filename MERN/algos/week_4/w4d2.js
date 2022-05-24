/*          __                        __         
           /\ \                      /\ \        
 _ __    __\ \ \___      __      ____\ \ \___    
/\`'__\/'__`\ \  _ `\  /'__`\   /',__\\ \  _ `\  
\ \ \//\  __/\ \ \ \ \/\ \L\.\_/\__, `\\ \ \ \ \ 
 \ \_\\ \____\\ \_\ \_\ \__/.\_\/\____/ \ \_\ \_\
  \/_/ \/____/ \/_/\/_/\/__/\/_/\/___/   \/_/\/_/

    Given to a Coding Dojo alumni by Riot Games.
    Rehash an incorrectly hashed string by combining letter count occurrences
    and alphabetizing them.
*/
//                 v
const str1 = "b70a164c32a20c10";
const expected1 = "a184b70c42";

function rehash(str) {
    let hashmap = {} //frequency table for our letters
    let allLetters = [] // will store each unique letter so that we can later sort
    let curLetter = str[0] // assumes first character is a letter
    let curVal = "" //we will need to concat to build this as we iterate
    let output = "" // string to return at the end

    for (let i = 1; i < str.length; i++) { //main loop through the string

        /* Handle current char */
        if (isNaN(str[i])) { // when we find a letter
            curLetter = str[i] //reset current letter
        } else { //otherwise found a number, keep building value string
            curVal += str[i]
        }

        /* Hashmap Logic */
        if (isNaN(str[i + 1])) { //triggers if the NEXT item isNaN (a letter, or undefined at the end)
            // i.e, we have all the info for a letter - value pair
            if (hashmap.hasOwnProperty(curLetter)) { //check our hashmap for our current letter
                hashmap[curLetter] += +curVal //update it if it exists by adding current value
            } else { // ( +curVal handles type conversion to number)
                hashmap[curLetter] = +curVal //create it if it does not exist
                allLetters.push(curLetter) //since it's new, add the letter to our array of letters
            }
            curVal = "" //reset current value string
        }
    }

    allLetters.sort() // sort all letters alphabetically

    for (let letter of allLetters) { //looping through our sorted letters
        output += `${letter}${hashmap[letter]}` //building our output string
    }

    return output
}

console.log(rehash(str1));
console.log(rehash(str1) === expected1, "<-- should be \"true\"");