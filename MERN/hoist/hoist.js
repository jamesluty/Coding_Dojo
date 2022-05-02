// // number 1
// var hello;

// // console.log(hello);
// hello = 'world';

// // output = undefined


// // number 2
// var needle;
// function test(){
//     var needle = 'magnet';
//     console.log(needle);
// }

// needle = 'haystack';
// // test();
// function test(){
//     var needle;

//     needle = 'magnet';
//     console.log(needle);
// }

// // output = magnet


// // number 3
// var brendan;
// function print(){
//     brendan = 'only okay';
//     console.log(brendan);
// }

// brendan = 'super cool';
// function print(){
//     brendan = 'only okay';
//     console.log(brendan);
// }
// // console.log(brendan);

// // output = super cool


// // number 4
// var food;
// function eat(){
//     food = 'half-chicken';
//     console.log(food);
//     var food = 'gone';
// }

// food = 'chicken';
// // console.log(food);
// // eat();
// function eat(){
//     var food;

//     food = 'half-chicken';
//     console.log(food);
//     food = 'gone';
// }

// output = chick, half-chicken


// number 5
// var mean;

// mean();
// console.log(food);
// mean = function() {
//     var food;

//     food = "chicken";
//     console.log(food);
//     food = "fish";
//     console.log(food);
// }
// console.log(food);

// output = error mean() is not a function


// number 6
// var genre;
// function rewind() {
//     genre = "rock";
//     console.log(genre);
//     var genre = "r&b";
//     console.log(genre);
// }

// console.log(genre);
// genre = "disco";
// rewind();
// function rewind() {
//     var genre;

//     genre = "rock";
//     console.log(genre);
//     genre = "r&b";
//     console.log(genre);
// }
// console.log(genre);

// output = undefined, rock, r&b, disco


// number 7
// var dojo;
// function learn() {
//     dojo = "seattle";
//     console.log(dojo);
//     var dojo = "burbank";
//     console.log(dojo);
// }

// dojo = "san jose";
// console.log(dojo);
// learn();
// function learn() {
//     var dojo;

//     dojo = "seattle";
//     console.log(dojo);
//     dojo = "burbank";
//     console.log(dojo);
// }
// console.log(dojo);

// output = san jose, seattle, burbank, san jose


// number 8 
function makeDojo(name, students){
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if(dojo.students > 50){
        dojo.hiring = true;
    }
    else if(dojo.students <= 0){
        dojo = "closed for now";
    }
    return dojo;
}

console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));
function makeDojo(name, students){
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if(dojo.students > 50){
        dojo.hiring = true;
    }
    else if(dojo.students <= 0){
        dojo = "closed for now";
    }
    return dojo;
}

// output = dojo{'name': chicago, 'students': 65, 'hiring': ture}, error on second console log, can not change const