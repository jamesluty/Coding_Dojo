class Ninja {
    constructor(name, health, speed=3, strength=3) {
        this.name = name;
        this.health = health;
        this.speed = speed;
        this.strength = strength;
    }

    // sayName method
    sayName() {
        console.log("Name: " + this.name);
    }

    // showStats method
    showStats() {
        console.log("Name: " + this.name);
        console.log("Strength: " + this.strength);
        console.log("Speed: " + this.speed);
        console.log("Health: " + this.health);
    }

    // drinkSake() method
    drinkSake() {
        this.health += 10;
    }
}

const ninja1 = new Ninja("Hyabusa", 100)
ninja1.sayName();
ninja1.showStats();

class Sensei extends Ninja {
    constructor(name, health=200, speed=10, strength=10, wisdom=10) {
        super(name, health, speed, strength);
        this.wisdom = wisdom;
    }

    // speakWisdom method
    speakWisdom() {
        super.drinkSake();
        console.log("A setback is just a setup for a comeback");
    }
}

const superSensei = new Sensei("Master Splinter");
superSensei.speakWisdom();
superSensei.showStats();