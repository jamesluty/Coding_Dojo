/*
  Given an array of ailments (illnesses), and an array of medication objects that have a nested array of treatedSymptoms
  return the medication name(s) that treats the most given symptoms
*/

const medications = [
    {
        name: "Sulforaphane",
        treatableSymptoms: [
            "dementia",
            "alzheimer's",
            "inflammation",
            "neuropathy",
        ],
    },
    {
        name: "Longvida Curcumin",
        treatableSymptoms: [
            "pain",
            "inflammation",
            "depression",
            "arthritis",
            "anxiety",
        ],
    },
    {
        name: "Hericium erinaceus",
        treatableSymptoms: [
            "anxiety",
            "cognitive decline",
            "depression"],
    },
    {
        name: "Nicotinamide mononucleotide",
        treatableSymptoms: [
            "ageing",
            "low NAD",
            "obesity",
            "mitochondrial myopathy",
            "diabetes",
        ],
    },
    {
        name: "PainAssassinator",
        treatableSymptoms: [
            "pain",
            "inflammation",
            "cramps",
            "headache",
            "toothache",
            "back pain",
            "fever",
        ],
    },
];


/*
Input: ["pain"], medications
Output: ["PainAssassinator", "Longvida Curcumin"]
*/

/*
Input: ["pain", "inflammation", "depression"], medications
Output: ["Longvida Curcumin"]
*/

/*
Input: ["existential dread"], medications
Output: []
*/

// HINTS:
// Loop through first array to check the medicine
// then loop through second array to see if the symptoms match the inputted symptoms
// if they match add them into a new array at the end return array
// edge case if no matches return null
function webMD(ailments, meds) {
    let symFreqObj = {}; // declare an obj to store med name and count
    for(let med of meds){ // Loop over array of objs
        for(let ailment of ailments){ // Loop over ailments
            if(med.treatableSymptoms.includes(ailment)){ // check if med treatableSymptoms contains ailment
                if(symFreqObj.hasOwnProperty(med.name)){ // check if symFreqObj has ailment key
                    symFreqObj[med.name] += 1; // increment value by 1 if exist
                } else {
                    symFreqObj[med.name] = 1; // add and set to 1 if not exists already
                }
            }
        }
    }

    let results = []; // declare a results array to return later
    let maxSym = 0; // declare a count variable to track max count
    for(let name in symFreqObj){ // loop over obj on symFreqObj
        if(symFreqObj[name] > maxSym){ // check if count value is greater then current maxSym
            results = []; // reset results array
            results.push(name); // add med name to array
            maxSym = symFreqObj[name] // change maxSym count
        } else if (symFreqObj[name] == maxSym){ // check if count value is equal to current maxSym
            results.push(name); // add med name to array
        }
    }
    return results // return results array
}

console.log(webMD(["pain"], medications));
console.log(webMD(["pain", "inflammation", "depression"], medications));
console.log(webMD(["existential dread"], medications));