var options = {
    crust: ["deep dish", "handtossed", "thin crust"],
    sauce: ["traditional", "marinara"],
    cheese: ["mozzarella", "feta", "cheedar"],
    toppings: ["pepperoni", "sausage", "mushrooms", "olives", "onions", "bacon"]
}

function pizzaOven(crust, sauce, cheese, toppings){
    var pizza = {};
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheese = cheese;
    pizza.toppings = toppings;
    return pizza;    
}

function rand(arr) {
    return Math.floor(Math.random() * arr.length);
}

var pizza1 = pizzaOven("deep dish", "traditional", "mozzarella", ["pepperoni", "sausage"]);
console.log(pizza1);

var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(pizza2);

var pizza3 = pizzaOven("deep dish", "traditional", "mozzarella");
console.log(pizza3);

var pizza4 = pizzaOven("thin crust", "marinara", "feta", ["pepperoni", "mushrooms"]);
console.log(pizza4);

var randPizza = pizzaOven(options.crust[rand(options.crust)], options.sauce[rand(options.sauce)], options.cheese[rand(options.cheese)], options.toppings[rand(options.toppings)]);
console.log(randPizza);