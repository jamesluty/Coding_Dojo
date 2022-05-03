class Ninja {
    constructor(name, health, speed=3, strength=3) {
        this.name = name;
        this.health = health;
        this.speed = speed;
        this.strength = strength;
    }

    // sayName method
    sayName() {
        console.log("Name: ${this.name}.");
    }

    // showStats method
    showStats() {
        console.log("Name: ${this.name}, Strength: ${this.stength}, Speed: %{this.speed}, Health: ${this.health}");
    }

    // drinkSake() method
    drinkSake() {
        this.health += 10;
    }
}