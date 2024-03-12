#!/usr/bin/node



class Shape {
    name;
    sides;
    sideLength;

    constructor(name, sides, sideLength) {
        this.name = name;
        this.sides = sides;
        this.sideLength = sideLength;
    }

    calcPerimeter() {
        let perimeter = this.sides * this.sideLength; // Calculate perimeter
        console.log(`${this.name} perimeter: ${perimeter}`);
    }
}

const square = new Shape("square", 4, 5);
square.calcPerimeter(); // Output: square perimeter: 20

const triangle = new Shape("triangle", 3, 3);
triangle.calcPerimeter(); // Output: triangle perimeter: 9
