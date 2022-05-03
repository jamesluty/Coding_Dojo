class Card {
    constructor(name, cost){
        this.name = name;
        this.cost = cost;
    }
}

class Unit extends Card {
    constructor(name, cost, power, resilience) {
        super(name, cost); 
        this.power = power;
        this.resilience = resilience;
    }

    attack(target) {
        if ( target instanceof Unit){
            target.resilience -= this.power;
            console.log(`${ this.name} attacked ${target.name} and lowered their resilience by ${target.resilience}`);
        } else {
            throw new Error(`${target} is not a unit`);
        }
    }
}

class Effect extends Card {
    constructor(name, cost, text, stat, magnitude) {
        super(name, cost);
        this.text = text;
        this.stat = stat;
        this.magnitude = magnitude;
    }

    play( unit ) {
        if ( unit instanceof Unit){
            if (this.stat === "power"){
                unit.power += this.magnitude
            } else if (this.stat === "resilience") {
                unit.resilience += this.magnitude
            }
            console.log(`${unit.name} played ${this.name} to ${this.text}`);
        } else {
            throw new Error(`${unit} is not a valid unit`);
        }
    }
}

let unit_red = new Unit("Red Belt Ninja", 3, 3, 4);
let unit_black = new Unit("Black Belt Ninja", 4, 5, 4);

let effect_hard_algo = new Effect("Hard Algorithm", 2, "increase target's resilience by 3", "resilience", 3);
let effect_unhandled_promise_rej = new Effect("Unhandled Promise Rejection", 1, "reduce target's resilience by 2", "resilience", -2);
let effect_pair_programming = new Effect("Pair Programming", 3, "increase target's power by 2", "power", 2);

effect_hard_algo.play(unit_red);
effect_unhandled_promise_rej.play(unit_red);
effect_pair_programming.play(unit_red);
unit_red.attack(unit_black);
