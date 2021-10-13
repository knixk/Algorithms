//  Problem from HackerRank 10 Days of JavaScript.

class Polygon {
    constructor(arr) {
        this.edges = arr;
    }
    
    perimeter() {
        let sum = 0;
        for (let i = 0; i < this.edges.length; i++) {
            sum += this.edges[i];
            // console.log("I am I at", i, this.edges[i])
        }
        return sum;
    }
}
